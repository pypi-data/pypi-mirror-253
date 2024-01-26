import json
import os
import string
import hashlib
import shutil
from .str import decimal_to_short_str
from .shell import shell_wrapper, shell_with_input, shell_result, shell_exitcode, shell_output
from .file import read_text, write_file, read_lines

last_docker_login_prefix = None


def docker_get_login_last_prefix():
    return last_docker_login_prefix


suffix_docker_hub_registry = '__docker_hub_registry'


def docker_env_registries(environ=None):
    environ = environ or os.environ
    result = set()
    for key in environ.keys():
        if key.endswith(suffix_docker_hub_registry):
            result.add(key[:-len(suffix_docker_hub_registry)])
    return sorted(result)


def docker_login_all_env(environ=None):
    for registry in docker_env_registries(environ):
        docker_login_env(environ, prefix=registry)


def docker_login_env(environ=None, prefix=None, try_skip=False):
    environ = environ or os.environ
    prefix = prefix or environ.get('DOCKER_LOGIN_PREFIX', '')
    if try_skip and prefix == docker_get_login_last_prefix():
        return
    docker_login(
        environ[prefix + suffix_docker_hub_registry],
        environ[prefix + '__docker_hub_username'],
        environ[prefix + '__docker_hub_password']
    )
    global last_docker_login_prefix
    last_docker_login_prefix = prefix


def docker_login(registry, username, password):
    print(F"Login to {registry} {username[0]}***{username[-1]} {password[0]}***{password[-1]}")
    ret, _, err = shell_with_input(f'docker login {registry} -u {username} --password-stdin', password)
    if ret:
        for mark in [b'net/http: TLS handshake timeout']:
            if mark in err:
                shell_wrapper('sleep 1')
                print(err, flush=True)
                docker_login(registry, username, password)
                break
        else:
            raise ChildProcessError(err)


def docker_pull(image):
    ret, err = shell_result(f'docker pull {image}')
    if ret:
        for mark in ['net/http: TLS handshake timeout']:
            if mark in err:
                shell_wrapper('sleep 1')
                docker_pull(image)
                break
        else:
            raise ChildProcessError(err)


def docker_push(image):
    ret, err = shell_result(f'docker push {image}')
    if ret:
        for mark in ['net/http:', 'dial tcp:']:
            if mark in err:
                shell_wrapper('sleep 1')
                print(err, flush=True)
                docker_push(image)
                break
        else:
            raise ChildProcessError(err)


def docker_remove(image):
    shell_wrapper(f'docker rmi {image}')


def docker_tag(image, new_image):
    shell_wrapper(f'docker tag {image} {new_image}')


def docker_build(image, path, args=None):
    result = ''
    if args:
        for k, v in args.items():
            result += f' --build-arg {k}={v}'
    shell_wrapper(f'echo "docker building..." && docker build -t {image} {result} {path}')


def docker_image_exist(image):
    return shell_exitcode(f'skopeo --override-os linux inspect docker://{image}') == 0


def docker_image_tags(image):
    result = shell_output(f"skopeo --override-os linux list-tags docker://{image}")
    return json.loads(result)['Tags']


docker_image_tag_max_length = 128


def format_image_url(url):
    sha256 = '@sha256'
    repo, tag = url.split(':', 1)
    if repo.endswith(sha256):
        repo = repo[:-len(sha256)]
    return ':'.join([repo.replace('.', '-').replace('/', '-'), tag])


def full_image_url(full_url):
    if ':' not in full_url:
        full_url = f'{full_url}:latest'
    r = full_url.split('/')
    if len(r) <= 1 or '.' not in r[0]:
        return f'docker.io/{full_url}'
    return full_url


def is_image_in_standard(url):
    return full_image_url(url).startswith('docker.io')


def omit_image_url(url):
    if ':' in url:
        repo, tag = url.split(':', 1)
    else:
        repo, tag = url, 'latest'
    repo = repo[repo.rfind("/", None, repo.rfind('/') - 1) + 1:]
    return ':'.join([repo.replace('.', '-').replace('/', '-'), tag])


def image_url_to_tag(full_url):
    full_url = full_image_url(full_url)
    tag = omit_image_url(full_url).replace(':', '-')
    if len(tag) > docker_image_tag_max_length:
        return decimal_to_short_str(
            int(hashlib.md5(full_url.encode('utf-8')).hexdigest(), 16),
            string.digits + string.ascii_letters + '_'
        )
    else:
        return tag


def container_image(full_url, all_in_one=''):
    full_url = full_image_url(full_url)
    if all_in_one:
        image_full_url = f'{all_in_one}:{image_url_to_tag(full_url)}'
    else:
        image_full_url = full_url
    registry, repository_tag = image_full_url.split('/', 1)
    repository, tag = repository_tag.split(':')
    return dict(
        image=image_full_url,
        registry=registry,
        repository=repository,
        rr=f'{registry}/{repository}',
        tag=tag
    )


def get_container_bin():
    for exe in ['nerdctl', 'podman', 'docker']:
        if shutil.which(exe):
            return exe


def docker_build_steps(image, image_step, path, args=None):
    def _do_prepare(x):
        write_file(os.path.join(path, 'Dockerfile'), x)

    def _do_build(target):
        shell_wrapper(f'docker build -t {target} {build_args} {path}')

    def _do_build_build():
        for i, c in enumerate(content_build):
            _do_prepare('\n'.join([content_args, c]))
            _do_build(f'build:cache--{i}')

    def _do_build_result():
        last_image = None
        has_updated = False
        for i, c in enumerate(content_result):
            is_last = i == len(content_result) - 1
            build_from = [f'FROM build:cache--{i} AS build{i}' for i in range(len(content_build))]
            if is_last:
                current_image = image
            elif i == 0:
                current_image = f'result-base-{result_little_version.get(i, 0)}'
            else:
                current_image = f'{image_step}--step-{i}-{result_little_version.get(i, 0)}'
            self_from = ''
            if last_image:
                self_from = f'FROM {last_image}'
            last_image = current_image
            if is_last or has_updated or not docker_image_exist(current_image):
                _do_prepare('\n'.join([content_args, *build_from, self_from, c]))
                _do_build(current_image)
                docker_push(current_image)
                has_updated = True

    content_args = ''
    content_build = {}
    content_result = {}
    for file in os.listdir(path):
        pa = os.path.join(path, file)
        if file.endswith('.Dockerfile'):
            name = '.'.join(file.split('.')[1:-1])
            content = read_text(pa)
            if file.startswith('args.'):
                content_args = content
            elif file.startswith('build.'):
                content_build[int(name)] = content
            elif file.startswith('result.'):
                content_result[int(name)] = content
    content_build = [content_build[i] for i in sorted(content_build)]
    content_result = [content_result[i] for i in sorted(content_result)]

    result_little_version = {
        i: int(x) for i, x in
        enumerate(read_lines(os.path.join(path, 'result.update'), skip_empty=True))
    }

    build_args = ''
    if args:
        if isinstance(args, str):
            build_args = args
        else:
            for k, v in args.items():
                build_args += f' --build-arg {k}={v}'

    _do_build_build()
    _do_build_result()
