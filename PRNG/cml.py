from pyfiglet import Figlet
import click
import os

# Paths to the folders
test_path = "sts-2.1.2/src"
program_path = "cmake-build-debug/"
output_path = "output/"

# Programs path
c_program = "prng"

# Files path
output_file = "output.txt"


@click.group()
def main():
    pass


@main.command(help='Run the C code')
@click.option('--all', '-a', is_flag=True, help='Run the Make file and Make clean')
@click.option('--make', '-m', is_flag=True, help='Run the Make file')
@click.option('--clean', '-c', is_flag=True, help='Run the Make Clean file')
def run(all, make, clean):
    click.echo("Running all the C files")

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
# @click.option("--name", prompt="Your name", help="The person to greet.")
@click.option("--name", default="Fran", help="The person to greet.")
def test(all, name):
    if all:
        click.echo("Running all the tests")
    else:
        click.echo('Hello %s!' % name)


if __name__ == '__main__':
    # Useless cool text
    f = Figlet(font='slant')
    print(f.renderText('PRNG'))

    main()

    while True:
        # Get a valid test messages
        while True:
            print("Which test do you want to run?")
            test = input("Test: ")

            # Check for invalid inputs
            if test:
                break
            else:
                print("Test not valid\n")

        stop = input("Insert stop to exit (nothing to continue): ")
        if stop == "stop":
            break
