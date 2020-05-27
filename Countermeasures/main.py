import click
from pyfiglet import Figlet

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
    ctx.invoke(keys)
    return 0


@main.command(help='')
@click.pass_context
def run():
    """

    """
    # ctx.invoke(keys)

    return 0


@main.command(help='Creates the RSA key and saves them in a csv file')
def keys():
    """
    Generates the RSA Keys
    """
    e_list = generate_e()  # Generates all the values for the exponent value
    key_size = generate_key_size()  # Generates all the values for the key size value
    key_list = generate_rsa_keys(e_list, key_size)  # Creates the list of keys
    save_keys(key_list)  # Save the keys to a csv file
    return 0


@main.command(help='Load the RSA keys from a csv file')
def load():
    """
    Generates the RSA Keys
    """
    key_list = load_keys()
    key_list[0].toString()
    return 0


f = Figlet(font='slant')  # Useless cool text
print(f.renderText('RSA Analysis'))

main()  # Runs the cli

# print(e)

# print("n: {}".format(n))
# print("e: {}".format(e))
# print("d: {}".format(d))
# print("msg: {}".format(msg))

# enc = square_mult(msg, e, n)

# print("enc: {}".format(enc))

# dec = square_mult(enc, d, n)

# print("dec: {}".format(dec))
