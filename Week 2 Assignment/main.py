import logging
import os
import re
import sys
from pathlib import Path
from numpy import clongdouble

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


def read_file_lines(file_path):
    with open(file_path) as file:
        return list(map(lambda line: line.strip(), file.readlines()))


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


def is_processed_file(file_path):
    return file_path in read_file_lines("NYL.lst")


def validate_phonenumbers(df: DataFrame, col_name):
    pattern = r"\d{3}\.\d{3}\.\d{4}"
    regex = re.compile(pattern)

    for i, number in enumerate(df[col_name]):
        if not regex.match(number):
            logging.warn(f"Invalid number {number} at row {i}")


def validate_emails(df: DataFrame, col_name):
    pattern = r".+@.+"
    regex = re.compile(pattern)

    for i, email in enumerate(df[col_name]):
        if not regex.match(email):
            logging.warn(f"Invalid email {email} at row {i}")


def validate_states(df: DataFrame, col_name):
    valid = read_file_lines("states.txt")

    for i, state in enumerate(df[col_name]):
        if state not in valid:
            logging.warn(f"Invalid state {state} found at row {i}")


def replace_headers(df: DataFrame):
    replacements = [
        ("Agent Writing Contract Start Date (Carrier appointment start date)",
         "Agent Writing Contract Start Date"),
        ("Agent Writing Contract Status (actually active and cancelled\'s should come in two different files)",
            "Agent Writing Contract Status")
    ]

    for (before, after) in replacements:
        if before in df.columns:
            df[before].rename(after)

    return df


def process_file(df: DataFrame):
    df = replace_headers(df)

    validate_phonenumbers(df, "Agency Phone Number")
    validate_states(df, "Agency State")
    validate_emails(df, "Agent Email Address")

    return df


if __name__ == "__main__":
    try:
        files = get_ordered_files("in")
        variance = line_diff(files[-1], files[-2])

        if variance > 500:
            raise "Line variance is too long. Could not process file"

        if is_processed_file(files[-1].as_posix()):
            raise "File has already been processed"

        write_to_file("NYL.lst", files[-1].as_posix())

        file_df = pd.read_csv(files[-1])
        processed = process_file(file_df)

        print(processed)
    except:
        logging.exception("")
