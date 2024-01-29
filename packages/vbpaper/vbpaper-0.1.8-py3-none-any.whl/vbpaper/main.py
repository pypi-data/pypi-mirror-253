import click

from .start import start
from .render import render

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