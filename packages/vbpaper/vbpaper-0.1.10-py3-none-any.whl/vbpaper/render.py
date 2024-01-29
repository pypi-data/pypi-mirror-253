import click
import os

@click.command(
        help="Renders pngs into pdf"
        )
@click.option(
    '-t',
    '--title',
    type=str,
    default='Plant Morphology',
    show_default=True,
    help="Title"
    )
@click.option(
    '-n',
    '--no_of_pngs',
    type=int,
    default=1,
    show_default=True,
    help="No of pngs"
    )
def render(title, no_of_pngs):
    """Renders pngs into pdf"""
    from .functions import create_main_tex_file, render_to_pdf
    cwd = os.getcwd()
    create_main_tex_file(cwd, title, no_of_pngs)
    render_to_pdf(cwd)
    click.echo('Paper rendered successfully')
