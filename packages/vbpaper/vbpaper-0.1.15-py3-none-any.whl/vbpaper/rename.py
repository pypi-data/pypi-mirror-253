import click
import os
from .functions import rename_screen_shoots


@click.command(
        help="renames screen shoots"
        )
def rename():
    """renames screen shoots"""
    cwd = os.getcwd()
    rename_screen_shoots(cwd)
    click.echo('Screen shoots renamed successfully')

