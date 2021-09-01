import click
import pyperclip
from create_password import create_password

# Create main group called cli
# This will be the root group


@click.group(name="Password generator")
@click.version_option("1.0.0")
def cli():
    pass


# Create main command called generate
@click.command(name="generate")
@click.option("--length", "-l",  show_default=True, default=10, type=(int), help="length of password")
@click.option("--save", "-s", is_flag=True, help="save password to passwords.txt")
@click.option("--no-numbers", "-nn", is_flag=True, help="generate wihout numbers")
@click.option("--no-symbols", "-ns", is_flag=True, help="generate without symbols")
def generate(length, save, no_numbers, no_symbols):
    password = create_password(length, no_numbers, no_symbols)

    pyperclip.copy(password)

    click.echo(
        f"{click.style('Generated password:', fg='green')} {click.style(password, bold=True)} {click.style('Copied to clipboard', bg='yellow', fg='black')}")


# Add commands to main group (cli)
cli.add_command(generate)

if __name__ == "__main__":
    cli()
