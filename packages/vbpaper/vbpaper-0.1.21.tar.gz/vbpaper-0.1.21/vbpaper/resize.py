import click
import os

@click.command(
        help="Resize the screen shoots"
        )
def resize():
    """Resize the screen shoots"""
    from .functions import extend_images
    cwd = os.getcwd()
    extend_images(cwd)
    click.echo('Screen shoots resized successfully')