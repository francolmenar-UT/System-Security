import click
from pyfiglet import Figlet

from src.algorithms.square_mult import square_mult
from src.graph.createGraph import create_graph
from src.functions.crypto import generate_e, generate_key_size, generate_rsa_keys, save_keys, load_keys


@click.group()
def main():
    pass


@main.command(help='')
@click.pass_context
def all(ctx):
    """
    Executes the run and test commands.
    Run: It uses the flags for performing a make clean & make all
    Test: It uses the flags for performing a make clean & make all and inside_c to set correctly the paths
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
    key_list = []
    if key:  # Generate the keys
        key_list = ctx.invoke(keys)
    elif load:  # Load the keys
        key_list = load_keys()

    square_mult(key_list)  # Execute

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
    # TODO
    create_graph()
    return 0


f = Figlet(font='slant')  # Useless cool text
print(f.renderText('RSA Analysis'))

main()  # Runs the cli
