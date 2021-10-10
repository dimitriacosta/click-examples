# pylint: disable=C0103
"""
Click multiple values from environment variables
"""
import click  # pylint: disable=E0401


@click.command()
@click.option('--path', 'paths', envvar='PATHS', multiple=True, type=click.Path())
def perform(paths):
    """Starts CLI application"""
    for path in paths:
        click.echo(path)


if __name__ == '__main__':
    perform()  # pylint: disable=E1120
