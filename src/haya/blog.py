from pathlib import Path
import shutil
from typing import Tuple, Any
from datetime import datetime
from haya.writer import PageWriter

type Item = Tuple[datetime, dict]
type Index = list[Item]


def parse_post_filename(filename: str) -> datetime:
    date = filename.split(".")[0].split("_")[0]
    return datetime.strptime(date, "%Y-%m-%d")

def make_index(
    index_folder: str, input_dir: Path, output_dir: Path, template_dir: Path
) -> Index:
    """Makes an index i.e. list of Tuple[datetime, str],
    while at the same time publishing the contents of the index"""

    index = []

    input_index = input_dir / index_folder
    output_index = output_dir / index_folder[1:]

    for rst in input_index.glob("*.rst"):
        date = parse_post_filename(rst.name)
        metadata = PageWriter(str(input_index), str(output_index), str(template_dir), rst.stem).write_page()
        metadata['path'] = '/' + str(Path(index_folder[1:]) / (rst.stem + '.html'))
        index.append((date, metadata))

    index.sort(reverse=True, key=lambda x: x[0])
    return index
