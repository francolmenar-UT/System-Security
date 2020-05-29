import timeit

import click
from pyfiglet import Figlet
from src.constants.constants import *

from src.CPA.CPA import cpa

from src.functions.func import *


from src.graph.createGraph import create_graph


@click.group()
def main():
    pass


@main.command(help='')
@click.option('--loop', '-l', is_flag=True, help='Run all values up to traces and subkey')
@click.option('--traces', '-t', required=False, nargs=1)
@click.option('--subkey', '-k', required=False, nargs=1)
@click.option('--step', '-st', required=False, nargs=1)
@click.option('--online', '-o', is_flag=True, required=False, nargs=1)
@click.pass_context
def both(ctx, loop, traces=None, subkey=None, step=None, online=False):
    ctx.invoke(run, loop=loop, traces=traces, subkey=subkey, step=step, online=False)
    ctx.invoke(run, loop=loop, traces=traces, subkey=subkey, step=step, online=True)


@main.command(help='')
@click.option('--loop', '-l', is_flag=True, help='Run all values up to traces and subkey')
@click.option('--traces', '-t', required=False, nargs=1, help='Amount of different traces used')
@click.option('--subkey', '-k', required=False, nargs=1)
@click.option('--step', '-st', required=False, nargs=1)
@click.option('--online', '-o', is_flag=True, required=False, nargs=1)
def run(loop, traces=None, subkey=None, step=None, online=False):
    data_list = []
    if all(v is not None for v in [loop, traces, subkey]):
        traces_step = CPA_N
        if step:
            traces_step = int(step)
        for i in range(1, int(subkey) + 1):
            j = traces_step
            while j <= int(traces) * traces_step + 1:
                best_guess, ge = cpa(j, i, online)

                exe_time = timeit.timeit(lambda: cpa(j, i, online), number=EXE_REP)
                data_list.append([i, j, exe_time/EXE_REP, best_guess, ge])

                j = j + traces_step

    elif all(v is not None for v in [traces, subkey]):
        best_guess, ge = cpa(int(traces), int(subkey), online)

        exe_time = timeit.timeit(lambda: cpa(int(traces), int(subkey), online), number=EXE_REP)
        data_list.append([int(subkey), int(traces), exe_time, best_guess, ge])

    elif traces is not None:
        best_guess, ge = cpa(int(traces), SUB_KEY_AMOUNT, online)

        exe_time = timeit.timeit(lambda: cpa(int(traces), SUB_KEY_AMOUNT, online), number=EXE_REP)
        data_list.append([SUB_KEY_AMOUNT, int(traces), exe_time, best_guess, ge])

    elif subkey is not None:
        best_guess, ge = cpa(NUM_TRACES, int(subkey), online)

        exe_time = timeit.timeit(lambda: cpa(NUM_TRACES, int(subkey), online), number=EXE_REP)
        data_list.append([int(subkey), NUM_TRACES, exe_time, best_guess, ge])

    else:
        best_guess, ge = cpa(NUM_TRACES, SUB_KEY_AMOUNT, online)

        exe_time = timeit.timeit(lambda: cpa(NUM_TRACES, SUB_KEY_AMOUNT, online), number=EXE_REP)
        data_list.append([SUB_KEY_AMOUNT, NUM_TRACES, exe_time, best_guess, ge])

    save_time(data_list, online)
    return 0


@main.command(help='Generates the Graphs from the data')
def graph():
    """
    Generates the Graphs
    """
    create_graph()
    return 0


f = Figlet(font='slant')  # Useless cool text
print(f.renderText('Online CPA'))

main()  # Runs the cli
