import click


@click.group()
def cli():
    pass


@cli.command()
def test():
    click.echo('hi')


if __name__ == '__main__':
    import ipdb;

    ipdb.set_trace()
    click
