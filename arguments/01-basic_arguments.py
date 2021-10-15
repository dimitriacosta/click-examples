# pylint: disable=C0103
"""
Click basic arguments
"""
import click  # pylint: disable=E0401


@click.command()
@click.argument('filename')
def touch(filename):
    """Print FILENAME"""
    click.echo(filename)


if __name__ == '__main__':
    touch()  # pylint: disable=E1120
