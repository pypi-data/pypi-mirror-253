import click

from .start import start
from .render import render
from .rename import rename

CONTEXT_SETTINGS = dict(
        help_option_names = [
            '-h',
            '--help'
        ]
)

@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    pass

main.add_command(start)
main.add_command(render)
main.add_command(rename)