# pylint: disable=C0103
"""
Click choice
"""
import click  # pylint: disable=E0401


@click.command()
@click.option('--hash-type', type=click.Choice(['MD5', 'SHA1'], case_sensitive=False))
def digest(hash_type):
    """Starts CLI application"""
    click.echo(hash_type)


if __name__ == '__main__':
    digest()  # pylint: disable=E1120
