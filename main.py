import click
from pyfiglet import Figlet

import timeit
# from src.graph.createGraph import create_graph

from src.pool import pool_atack


@click.group()
def main():
    pass


@main.command(help='')
def run():
    pool_atack()
    return 0


@main.command(help='Generates the Graphs from the data')
def graph():
    """
    Generates the Graphs
    """
    # create_graph()
    return 0


f = Figlet(font='slant')  # Useless cool text
print(f.renderText('Pooled Template Attack'))

main()  # Runs the cli
