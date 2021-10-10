# pylint: disable=C0103
"""
Click boolean flags
"""
import sys
import click  # pylint: disable=E0401


@click.command()
@click.option('--shout', is_flag=True)
def info(shout):
    """Starts CLI application"""
    rv = sys.platform
    if shout:
        rv = rv.upper() + '!!!!!'
    click.echo(rv)


if __name__ == '__main__':
    info()  # pylint: disable=E1120
