# pylint: disable=C0103
"""
Click basic value
"""
import click  # pylint: disable=E0401


@click.command()
@click.option('-f', '--from', 'from_') # from is a reserverd word in python so we use from_ instead
@click.option('-t', '--to')
def reserved_param_name(from_, to):
    """Starts CLI application"""
    click.echo(f"from {from_}, to {to}")


if __name__ == '__main__':
    reserved_param_name()  # pylint: disable=E1120
