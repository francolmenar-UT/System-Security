import click
from pyfiglet import Figlet
from processing import *
from test_handle import *


@click.group()
def main():
    pass


@main.command()
@click.option('--post', '-p', is_flag=True, help='Run van Neumann post processing')
@click.pass_context
def all(ctx, post):
    """
    Executes the run and test commands.
    Run: It uses the flags for performing a make clean & make all
    Test: It uses the flags for performing a make clean & make all and inside_c to set correctly the paths
    :param ctx: Context need to invoking commands
    """
    if post:  # Run using post processed data
        ctx.invoke(run, all=False, post=True)
    else:  # Not post processed data
        ctx.invoke(run, all=False)
    ctx.invoke(test, all=True, clean=True, make=True, inside_c=True)
    return 0


@main.command(help='Compiles the C code')
@click.option('--all', '-a', is_flag=True, help='Run the make clean && make')
@click.option('--clean', '-c', is_flag=True, help='Run the make clean')
@click.option('--make', '-m', is_flag=True, help='Run just make')
@click.option('--post', '-p', is_flag=True, help='Run van Neumann post processing')
def run(all, clean, make, post):
    """
    Compiles the C code
    """
    os.chdir(program_path)

    if all:
        os.system("make clean && make all")
    else:
        if clean:
            os.system("make clean")
        if make:
            os.system("make all")

    if post:  # Run using post processed data
        post_processing()

    else:  # Not post processed data
        os.system("./{} "
                  "{} {} "
                  "> {}{}".format(c_program,
                                  bit_streams, total_bit_length,  # Set the length of the output streams
                                  output_path, output_file))
    return 0


@main.command()
@click.option('--all', '-a', is_flag=True, help='Run all the tests')
@click.option('--clean', '-c', is_flag=True, help='Run the make clean')
@click.option('--make', '-m', is_flag=True, help='Run just make')
@click.option('--inside_c', is_flag=True, help='Just to be used from `all` command')
@click.argument('tests', type=str, nargs=-1)
def test(all, clean, make, tests, inside_c):
    """
    Process the input for running the tests and sends the data to test_handle()
    """
    if inside_c:  # It is called from "all". Sets the path to the correct place
        os.chdir(test_path_c)
    else:
        os.chdir(test_path)
    test_list = []
    if clean:
        os.system("make clean")
    if make:
        os.system("make")

    if all:  # Execute all the tests
        test_list = list(range(1, 15 + 1))  # Set the range of all the tests

    else:  # Execute only the given tests
        if len(tests) is 0:  # No test introduced
            click.echo('Incorrect test input: Please introduce a test number or a range (1-3)')
            return -1

        try:  # Convert the input ranges into a list of numbers
            for file in tests:
                range_split = file.split('-')  # Split the range tests

                if len(range_split) is 1:  # Check if it is a single value, not a range
                    test_list.append(int(range_split[0]))

                elif len(range_split) is 2:  # Check if it is in range format
                    list_tests = list(range(int(range_split[0]), int(range_split[1]) + 1))

                    for ti in list_tests:
                        test_list.append(ti)

                else:  # Wrong format
                    click.echo('Incorrect test input: Please introduce a test number or a range (1-3)')
                    return -1

        except ValueError:  # Wrong format
            click.echo('Incorrect test input: Please introduce a test number or a range (1-3)')
            return -1

    test_handle(test_list)  # Calls for executing the tests
    return 0


f = Figlet(font='slant')  # Useless cool text
print(f.renderText('PRNG'))

main()  # Runs the cli
