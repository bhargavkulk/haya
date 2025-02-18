from typing import *
import click
import tomllib
from pathlib import Path
import shutil
import sass
from haya.blog import make_index

from haya.writer import PageWriter

INPUT_DIR = Path('./content/')
OUTPUT_DIR = Path('./docs/')
TEMPLATE_DIR = Path('./templates/')
SCSS_DIR = Path('./scss/')
CSS_DIR = Path('./css/')

@click.group()
def main():
    pass

@click.command()
def build():
    if CSS_DIR.exists():
        shutil.copytree(CSS_DIR, OUTPUT_DIR / 'css')

    if SCSS_DIR.exists():
        sass.compile(dirname=(str(SCSS_DIR), (str(OUTPUT_DIR / 'css'))))

    indices = dict()

    # any folder that begins with _ is to treated
    # as something to be indexed.
    # The filenames have to follow a specific format:
    # YYYY-MM-DD_name.rst
    for tbi in INPUT_DIR.iterdir():
        if tbi.is_dir() and tbi.name.startswith("_"):
            index = make_index(tbi.name, INPUT_DIR, OUTPUT_DIR, TEMPLATE_DIR)
            indices[tbi.name] = index

    for rst_file in INPUT_DIR.glob('*.rst'):
        PageWriter(INPUT_DIR,
                   OUTPUT_DIR,
                   TEMPLATE_DIR,
                   rst_file.stem,
                   indices).write_page()


main.add_command(build)

if __name__ == "__main__":
    main()
