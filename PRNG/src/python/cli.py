from pyfiglet import Figlet
import click
import os

from constants import *
from test_handle import *


@click.group()
def main():
    pass


@main.command()
@click.pass_context
def call(ctx):
    # Test Command for later use
    click.echo("Call")
    ctx.invoke(run, all=True)


@main.command(help='Run the C code')
@click.option('--all', '-a', is_flag=True, help='Run the Make file and Make clean')
@click.option('--clean', '-c', is_flag=True, help='Run the Make Clean file')
@click.option('--make', '-m', is_flag=True, help='Run the Make file')
def run(all, clean, make):
    click.echo("Compiling xoroshiro128+")

    os.chdir(program_path)  # cd

    if all:
        os.system("make clean && make all")
    else:
        if clean:
            os.system("make clean")
        if make:
            os.system("make all")

    os.system("./" + c_program + " > " + "../" + output_path + output_file)


@main.command()
@click.option('--all', '-a', is_flag=True, help='Run all the tests or not')
@click.option('--clean', '-c', is_flag=True, help='Run the Make Clean file')
@click.option('--make', '-m', is_flag=True, help='Run the Make file')
@click.argument('tests', type=str, nargs=-1)
def test(all, clean, make, tests):
    os.chdir(test_path)
    test_list = []
    if clean:
        os.system("make clean")
    if make:
        os.system("make")
        
    if all:  # Execute all the tests
        click.echo("Running all the tests")
        test_list = list(range(1, 15 + 1))

    else:  # Execute only the given tests
        if len(tests) is 0:  # No test introduced
            click.echo('Incorrect test input: Please introduce a test number or a range (1-3)')
            return

        try:  # Convert the input ranges into a list of numbers
            for file in tests:
                range_split = file.split('-')  # Split the range tests

                if len(range_split) is 1:  # Check if it is a single value, not a range
                    test_list.append(range_split[0])

                elif len(range_split) is 2:  # Check if it is in range format
                    list_tests = list(range(int(range_split[0]), int(range_split[1]) + 1))

                    for ti in list_tests:
                        test_list.append(ti)

                else:  # Wrong format
                    click.echo('Incorrect test input: Please introduce a test number or a range (1-3)')
                    return

        except ValueError:
            click.echo('Incorrect test input: Please introduce a test number or a range (1-3)')
            return
    test_handle(test_list)


if __name__ == '__main__':
    # Useless cool text
    f = Figlet(font='slant')
    print(f.renderText('PRNG'))

    main()
