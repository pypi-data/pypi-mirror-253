import click
import os

@click.command(
        help="Resize the screen shoots"
        )
@click.option(
        '-s',
        '--scale_factor',
        type=float,
        default=1.5,
        show_default=True,
        help="Scale factor"
        )
def resize(scale_factor):
    """Resize the screen shoots"""
    from .functions import extend_images
    cwd = os.getcwd()
    extend_images(cwd, scale_factor=scale_factor)
    click.echo('Screen shoots resized successfully')