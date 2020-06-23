import click
from pyfiglet import Figlet

from src.constant.constant import *
from src.graph.createGraph import create_graph

from src.pool import pool_atack


@click.group()
def main():
    pass


@main.command(help='')
@click.pass_context
def both(ctx):
    # Run without noise
    ctx.invoke(run, noise=False)

    # Run with noise
    ctx.invoke(run, noise=True)


@main.command(help='')
@click.option('--noise', '-n', is_flag=True, help='Run the execution with noise')
def run(noise=False):
    # Firs Scenario

    rank_list_a = [pool_atack(PROFILE_0, ATTACK_0, noise)]

    # Result, GE, Best Guesses

    # print(rank_list_a[0])
    # print()
    # print(rank_list_a)
    # print()

    # Second Scenario

    rank_list_b = [pool_atack(PROFILE_1, ATTACK_1, noise)]

    # print(rank_list_b[0])
    # print()
    # print(rank_list_b)
    # print()

    return 0


@main.command(help='Generates the Graphs from the data')
def graph():
    """
    Generates the Graphs
    """
    create_graph()
    return 0


f = Figlet(font='slant')  # Useless cool text
print(f.renderText('Pooled Template Attack'))

main()  # Runs the cli
