import click
import os

@click.command(
        help="initiates the paper"
        )
def start():
    """initiates the paper"""
    from .functions import change_screen_shoot_location
    cwd = os.getcwd()
    change_screen_shoot_location(cwd)
    click.echo('Paper initiated successfully')