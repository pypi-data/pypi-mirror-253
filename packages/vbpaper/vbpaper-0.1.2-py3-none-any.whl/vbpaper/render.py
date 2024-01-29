import click

@click.command(
        help="Renders pngs into pdf"
        )
@click.option(
    '-d',
    '--dirpath',
    type=click.Path(),
    default='./',
    show_default=True,
    help="Directory path"
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
def render(dirpath, title, normalize):
    """Renders pngs into pdf"""
    from .functions import rename_screen_shoots, create_main_tex_file, render
    rename_screen_shoots(dirpath)
    create_main_tex_file(dirpath, title)
    render(dirpath)
    click.echo('Paper rendered successfully')
    
    if normalize:
        from .functions import back_to_normal
        back_to_normal()
        
        click.echo('Screen shoots directory normalized to Desktop successfully')
