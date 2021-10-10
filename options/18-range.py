# pylint: disable=C0103
"""
Click range
"""
import click  # pylint: disable=E0401


@click.command()
@click.option('--count', type=click.IntRange(0, 20, clamp=True))
@click.option('--digit', type=click.IntRange(0, 10))
def repeat(count, digit):
    """Starts CLI application"""
    click.echo(str(digit) * count)


if __name__ == '__main__':
    repeat()  # pylint: disable=E1120
