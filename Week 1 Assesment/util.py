import logging
import re
import sys
import pathlib
from datetime import datetime

import pandas as pd

from my_types import MonthYear


def get_console_input():
    args = sys.argv

    if pathlib.Path(args[1]).is_file:
        return args[1]

    logging.error(f"File does not exist: {args}")
    exit(1)


def get_sheet(file_path, sheet_name):
    logging.debug(f"Loading up {file_path} with sheet name {sheet_name}")

    with pd.ExcelFile(file_path) as xlsx:
        if sheet_name not in xlsx.sheet_names:
            logging.error(f"Failed to load sheet: {sheet_name}")
            exit(1)

        return pd.read_excel(xlsx, sheet_name)


def parse_date(month, year):
    try:
        logging.debug(f"parse_date with month: \"{month}\" year: \"{year}\"")
        return datetime.strptime(f"{month} {year}", "%B %Y")
    except:
        logging.error("Could not parse date")
        exit(1)


def get_month_year_from_file(file_path) -> MonthYear:
    logging.debug(f"Reading month and year from {file_path}")
    pattern = ".*_(?P<month>.*)_(?P<year>.*?)\.xlsx"
    result = re.search(pattern, file_path)

    if result == None:
        logging.error(
            f"Could not get the month and year from file: {file_path}")
        exit(1)

    return MonthYear(result.group("month"), result.group("year"))


def get_date_from_file(file_path):
    file_month, file_year = get_month_year_from_file(file_path)
    return parse_date(file_month, file_year)
