import click
from pyfiglet import Figlet

from src.algorithms.ladder import square_ladder
from src.algorithms.square_mult import square_mult
from src.algorithms.square_mult_alw import square_mult_alw
from src.functions.crypto import generate_e, generate_rsa_keys, save_keys, load_keys
from src.graph.createGraph import create_graph


@click.group()
def main():
    pass


@main.command(help='')
@click.pass_context
def all(ctx):
    """
    :param ctx: Context need to invoking commands
    """
    ctx.invoke(run, key=True)
    return 0


@main.command(help='')
@click.option('--key', '-k', is_flag=True, help='Generates the RSA keys')
@click.option('--load', '-l', is_flag=True, help='Loads the RSA keys')
@click.pass_context
def run(ctx, key, load):
    """
    # TODO
    """
    for i in range(0, 3):  # Ran the three algorithms
        key_list = []
        if key:  # Generate the keys
            key_list = ctx.invoke(keys)
        elif load:  # Load the keys
            key_list = load_keys()
        if i == 0:
            # square_mult(key_list)  # Execute 1
            print()
        elif i == 1:
            # square_mult_alw(key_list)  # Execute 2
            print()
        elif i == 2:
            square_ladder(key_list)  # Execute 3
    return 0


@main.command(help='Generates the RSA keys')
def keys():
    """
    Generates the RSA Keys
    """
    e_list = generate_e()  # Generates all the values for the exponent value
    key_list = generate_rsa_keys(e_list)  # Creates the list of keys
    save_keys(key_list)  # Save the keys to a csv file
    return key_list


@main.command(help='Generates the Graphs from the data')
def graph():
    """
    Generates the RSA Keys
    """
    create_graph()
    return 0


f = Figlet(font='slant')  # Useless cool text
print(f.renderText('RSA Analysis'))

main()  # Runs the cli
