import click
from pyfiglet import Figlet

from src.CPA import CPA


@click.group()
def main():
    pass


@main.command(help='')
def run():
    CPA()
    return 0


f = Figlet(font='slant')  # Useless cool text
print(f.renderText('Online CPA'))

main()  # Runs the cli
