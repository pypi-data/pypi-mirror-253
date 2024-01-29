import click

@click.command(
        help="Normalize the screen shoots directory"
        )
def normalize():
    """Normalize the screen shoots directory"""
    from .functions import back_to_normal
    back_to_normal()
    
    click.echo('Screen shoots directory normalized to Desktop successfully')