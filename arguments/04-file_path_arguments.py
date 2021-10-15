# pylint: disable=C0103
"""
Click file path argument
"""
import click  # pylint: disable=E0401


@click.command()
@click.argument('filename', type=click.Path(exists=True))
def touch(filename):
    """Print FILENAME if the file exists,"""
    click.echo(click.format_filename(filename))


if __name__ == '__main__':
    touch()  # pylint: disable=E1120
