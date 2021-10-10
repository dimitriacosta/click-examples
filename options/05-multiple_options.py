# pylint: disable=C0103
"""
Click multiple options
"""
import click  # pylint: disable=E0401


@click.command()
@click.option('--message', '-m', multiple=True)
def commit(message):
    """Starts CLI application"""
    click.echo('\n'.join(message))


if __name__ == '__main__':
    commit()  # pylint: disable=E1120
