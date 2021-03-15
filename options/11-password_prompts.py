import click

@click.command()
@click.password_option()
def encrypt(password):
    click.echo(f"Encrypting password to {password}")

if __name__ == '__main__':
    encrypt()
