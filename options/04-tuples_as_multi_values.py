# pylint: disable=C0103
"""
Click tuples as multi-values
"""
import click  # pylint: disable=E0401


@click.command()
@click.option('--item', type=(str, int))
def put_item(item):
    """Starts CLI application"""
    click.echo('name=%s id=%d' % item)


if __name__ == '__main__':
    put_item()  # pylint: disable=E1120
