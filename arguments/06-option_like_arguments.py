# pylint: disable=C0103
"""
Click option like arguments
"""
import click  # pylint: disable=E0401


@click.command()
@click.argument('files', nargs=-1, type=click.Path())
def touch(files):
    """Print all FILES names."""
    for filename in files:
        click.echo(filename)


if __name__ == '__main__':
    touch()  # pylint: disable=E1120
