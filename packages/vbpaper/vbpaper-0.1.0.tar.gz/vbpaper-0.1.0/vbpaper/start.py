import click

@click.command(
        help="initiates the paper"
        )
@click.option(
    '-d',
    '--dirpath',
    type=click.Path(),
    default='./',
    show_default=True,
    help="Directory path"
    )
def start(dirpath):
    """initiates the paper"""
    from .functions import change_screen_shoot_location
    change_screen_shoot_location(dirpath)
    click.echo('Paper initiated successfully')