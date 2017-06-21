import click


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    click.echo("Debug mode")


@cli.command()
def run():
    click.echo("run")

if __name__ == '__main__':
    cli.main(prog_name="demo1")
