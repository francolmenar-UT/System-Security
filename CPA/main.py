import click
from pyfiglet import Figlet
from src.constants.constants import *

from src.CPA.CPA import CPA


@click.group()
def main():
    pass


@main.command(help='')
def run():
    for i in range(1, 10):
        for j in range(1, 4):
            print("Execution: {}-{}".format(i, j))
            CPA(i, j * 5)
    return 0


f = Figlet(font='slant')  # Useless cool text
print(f.renderText('Online CPA'))

main()  # Runs the cli
