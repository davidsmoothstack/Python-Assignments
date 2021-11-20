import logging
import os
import sys
from pathlib import Path
from typing import List

import pandas as pd
from pandas.core.frame import DataFrame

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)


def get_ordered_files(dir_path):
    dir_path = Path(dir_path).resolve()

    if not dir_path.is_dir:
        raise f"{dir_path} is not a valid path"

    return sorted(
        map(lambda file_name:
            dir_path.joinpath(file_name), os.listdir(dir_path))
    )


def line_diff(path1, path2):
    with open(path1) as file1:
        with open(path2) as file2:
            count1 = len(open(path1).readlines())
            count2 = len(open(path2).readlines())

            return abs(count1 - count2)


def write_to_file(file_path, content):
    path = Path(file_path)

    if not path.exists():
        with open(path, "x") as file:
            file.write("")

    with open(path, "a") as file:
        file.write(content + "\n")


def validate_phonenumber(df: DataFrame):
    pattern = "\(?\(d{3})\)?(-|\s+)\1\2\d{4}"


def validate_email(df: DataFrame):
    pattern = ".+@.+"


def process_file(file_path):
    pass

# def replace_headers(csv_path):
#     replacements = {
#         "Agent Writing Contract Start Date (Carrier appointment start date)": "Agent Writing Contract Start Date",
#         "Agent Writing Contract Status (actually active and cancelled\'s should come in two different files)": "Agent Writing Contract Status"


if __name__ == "__main__":
    try:
        files = get_ordered_files("Week 2 Assignment/in")
        variance = line_diff(files[-1], files[-2])

        if variance > 500:
            logging.error("Line variance is too long. Could not process file")
            exit(1)

        write_to_file("NYL.lst", files[-1].as_posix())

    except:
        logging.exception("")
