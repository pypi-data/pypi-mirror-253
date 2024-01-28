import os
import typer
from ..file import normal_path, remove_path, FileHitChecker

app = typer.Typer(add_completion=False)


@app.command()
def remove(path, ignore='.rmignore'):
    def remove_dir(fp, is_hit, _):
        if not is_hit:
            remove_path(fp)

    path = normal_path(path)
    if os.path.isdir(path):
        FileHitChecker(path, ignore).walk(remove_dir)
    elif os.path.isfile(path):
        if not FileHitChecker(os.path.dirname(path), ignore).is_hit(path):
            remove_path(path)
