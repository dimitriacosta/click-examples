# pylint: disable=C0103
"""
Click multi value
"""
import click  # pylint: disable=E0401


@click.command()
@click.option('--pos', nargs=2, type=float, help="Insert two numbers")
def find_me(pos):
    """Starts CLI application"""
    click.echo('%s / %s' % pos)


if __name__ == '__main__':
    find_me()  # pylint: disable=E1120
