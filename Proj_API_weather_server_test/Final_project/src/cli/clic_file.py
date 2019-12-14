from src.prog_logic.main import Temp
from src.server.flask import app
import click

@click.group()
def cli():
    pass


# @click.command('today')
# @click.option('-t')
# def today_cli(t):
#     t = Temp()
#     print(t.today())
# cli.add_command(today_cli)


@click.command('week')
@click.option('-w')
def temp_five_day_cli(w):
    t = Temp()
    print(t.temp_five_day())
cli.add_command(temp_five_day_cli)



@cli.command("server")
def start_server():
    app.run(port=8080)

