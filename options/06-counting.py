# pylint: disable=C0103
"""
Click counting
"""
import click  # pylint: disable=E0401


@click.command()
@click.option('-v', '--verbose', count=True)
def log(verbose):
    """Starts CLI application"""
    click.echo(f"Verbosity level: {verbose}")


if __name__ == '__main__':
    log()  # pylint: disable=E1120
