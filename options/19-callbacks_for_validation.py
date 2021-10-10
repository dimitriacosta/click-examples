# pylint: disable=C0103
"""
Click callbacks from validation
"""
import click  # pylint: disable=E0401


def validate_rolls(ctx, param, value):  # pylint: disable=W0613
    """Validate rolls"""
    try:
        rolls, dice = map(int, value.split('d', 2))
        return dice, rolls
    except ValueError:
        raise click.BadParameter('rolls need to be in format NdM')  # pylint: disable=W0707


@click.command()
@click.option('--rolls', callback=validate_rolls, default='1d6')
def roll(rolls):
    """Starts CLI application"""
    click.echo('Rolling a %d-sliced dice %d time(s)' % rolls)


if __name__ == '__main__':
    roll()  # pylint: disable=E1120
