import click
import sys

@click.command()
@click.option('--path', 'paths', envvar='PATHS', multiple=True, type=click.Path())
def perform(paths):
    for path in paths:
        click.echo(path)

if __name__ == '__main__':
    perform()
