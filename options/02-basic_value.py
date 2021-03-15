import click

@click.command()
@click.option('-f', '--from', 'from_')
@click.option('-t', '--to')
def reserved_param_name(from_, to):
    click.echo(f"from {from_}, to {to}")

if __name__ == '__main__':
    reserved_param_name()
