import click
from application import app


@click.group()
def cli():
    pass

@click.command()
def run():
    app.run()

cli.add_command(run)

if __name__ == '__main__':
    cli()
