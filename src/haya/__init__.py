from typing import *
import click
import tomllib
from pathlib import Path
import sass

from haya.writer import PageWriter

INPUT_DIR = Path('./content/')
OUTPUT_DIR = Path('./docs/')
TEMPLATE_DIR = Path('./templates/')
SCSS_DIR = Path('./scss/')

@click.group()
def main():
    pass

@click.command()
def build():
    if SCSS_DIR.exists():
        sass.compile(dirname=(str(SCSS_DIR), (str(OUTPUT_DIR / 'css'))))

    for rst_file in INPUT_DIR.glob('*.rst'):
        PageWriter(INPUT_DIR,
                   OUTPUT_DIR,
                   TEMPLATE_DIR,
                   rst_file.stem).write_page()


main.add_command(build)

if __name__ == "__main__":
    main()
