# pylint: disable=C0103
"""
Click feature switches
"""
import sys
import click  # pylint: disable=E0401


@click.command()
@click.option('--upper', 'transformation', flag_value='upper', default=True)
@click.option('--lower', 'transformation', flag_value='lower')
def info(transformation):
    """Starts CLI application"""
    click.echo(getattr(sys.platform, transformation)())


if __name__ == '__main__':
    info()  # pylint: disable=E1120
