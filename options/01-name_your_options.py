import click

@click.command()
@click.option('--n', default=1, show_default=True)
def dots(n):
    click.echo('.' * n)

if __name__ == '__main__':
    dots()
