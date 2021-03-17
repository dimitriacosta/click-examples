import click

@click.command()
@click.option('+w/-w')
def chmod(w):
    click.echo(f"writable={w}")

if __name__ == '__main__':
    chmod()
