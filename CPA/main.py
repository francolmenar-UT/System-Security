import click
from pyfiglet import Figlet
from src.constants.constants import *

from src.CPA.CPA import CPA as CPA_py

from src.Online_CPA.online_CPA import online_CPA


@click.group()
def main():
    pass


@main.command(help='')
@click.option('--loop', '-l', is_flag=True, help='Run all values up to traces and subkey')
@click.option('--traces', '-t', required=False, nargs=1)
@click.option('--subkey', '-k', required=False, nargs=1)
@click.option('--step', '-st', required=False, nargs=1)
def CPA(loop, traces=None, subkey=None, step=None):
    if all(v is not None for v in [loop, traces, subkey]):
        traces_step = 5
        if step:
            traces_step = int(step)
        for i in range(1, int(subkey) + 1):
            j = traces_step
            while j <= int(traces) * traces_step + 1:
                CPA_py(j, i)
                j = j + traces_step
    elif all(v is not None for v in [traces, subkey]):
        CPA_py(int(traces), int(subkey))
    else:
        CPA_py(NUM_TRACES, SUB_KEY_AMOUNT)
    return 0


@main.command(help='')
@click.option('--loop', '-l', is_flag=True, help='Run all values up to traces and subkey')
@click.option('--traces', '-t', required=False, nargs=1)
@click.option('--subkey', '-k', required=False, nargs=1)
@click.option('--step', '-st', required=False, nargs=1)
def online(loop, traces=None, subkey=None, step=None):
    if all(v is not None for v in [loop, traces, subkey]):
        traces_step = 5
        if step:
            traces_step = int(step)
        for i in range(1, int(subkey) + 1):
            j = traces_step
            while j <= int(traces) * traces_step + 1:
                online_CPA(j, i)
                j = j + traces_step
    elif all(v is not None for v in [traces, subkey]):
        online_CPA(int(traces), int(subkey))
    else:
        online_CPA(NUM_TRACES, SUB_KEY_AMOUNT)
    return 0


f = Figlet(font='slant')  # Useless cool text
print(f.renderText('Online CPA'))

main()  # Runs the cli
