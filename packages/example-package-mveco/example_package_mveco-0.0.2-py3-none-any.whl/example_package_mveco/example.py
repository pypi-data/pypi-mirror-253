import click


@click.command()
@click.option('--name', default='World', help='The person to greet.')
def hello(name):
    click.echo(f'Hello, {name}!')


if __name__ == '__main__':
    hello()

