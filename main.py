import click
from pyfiglet import Figlet

import timeit
# from src.graph.createGraph import create_graph
from src.constant.constant import *

from src.pool import pool_atack


@click.group()
def main():
    pass


@main.command(help='')
def run():
    # List storing all the resulting key rank values from all the evaluations
    rank_list = []

    # Firs Scenario
    rank_list.append(pool_atack(PROFILE_0, ATTACK_0))

    print(rank_list)

    print(rank_list[0])

    # Second Scenario
    # pool_atack(PROFILE_1, ATTACK_1)
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
