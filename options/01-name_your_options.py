# pylint: disable=C0103
"""
Click name your options
"""
import click  # pylint: disable=E0401


@click.command()
@click.option('-n', '--number', default=1, show_default=True, help="How many dots do you want?")
def dots(number):
    """Starts CLI application"""
    click.echo('.' * number)


if __name__ == '__main__':
    dots()  # pylint: disable=E1120
