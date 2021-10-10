# pylint: disable=C0103
"""
Click password prompts
"""
import click  # pylint: disable=E0401


@click.command()
@click.password_option()
def encrypt(password):
    """Starts CLI application"""
    click.echo(f"Encrypting password to {password}")


if __name__ == '__main__':
    encrypt()  # pylint: disable=E1120
