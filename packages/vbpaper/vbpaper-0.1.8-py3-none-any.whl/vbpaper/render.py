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
    '--normalize',
    is_flag=True,
    default=False,
    show_default=True,
    help="Normalize the screen shoots directory"
    )
def render(title, normalize):
    
    if normalize:
        from .functions import back_to_normal
        back_to_normal()
        
        click.echo('Screen shoots directory normalized to Desktop successfully')
        
    else:
        """Renders pngs into pdf"""
        from .functions import rename_screen_shoots, create_main_tex_file, render
        cwd = os.getcwd()
        rename_screen_shoots(cwd)
        create_main_tex_file(cwd, title)
        render(cwd)
        click.echo('Paper rendered successfully')
