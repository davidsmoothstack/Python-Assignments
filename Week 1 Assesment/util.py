import logging
import pathlib
import re
import sys
from datetime import datetime

import pandas as pd

from my_types import MonthYear


def to_percent(float):
    return f"{float * 100}%"


def get_console_input():
    args = sys.argv

    if len(args) != 2:
        logging.error("Incorrent amount of arguments")
        exit(1)

    if not pathlib.Path(args[1]).is_file:
        logging.error(f"File does not exist: {args[1]}")
        exit(1)

    return args[1]


def get_sheet(file_path, sheet_name):
    """Returns an excel sheet from the specified file"""
    logging.debug(f"Loading up {file_path} with sheet name {sheet_name}")

    with pd.ExcelFile(file_path) as xlsx:
        if sheet_name not in xlsx.sheet_names:
            logging.error(f"Failed to load sheet: {sheet_name}")
            exit(1)

        return pd.read_excel(xlsx, sheet_name)


def get_datetime(month, year):
    """Generates a datetime object from the provided month and year"""
    try:
        logging.debug(f"parse_date with month: \"{month}\" year: \"{year}\"")
        return datetime.strptime(f"{month} {year}", "%B %Y")
    except:
        logging.error("Could not parse date")
        exit(1)


def get_month_year_from_file(file_path) -> MonthYear:
    """Generates a MonthYear tuple with a month and a year using the files name"""
    logging.debug(f"Reading month and year from {file_path}")
    pattern = ".*_(?P<month>.*)_(?P<year>.*?)\.xlsx"
    result = re.search(pattern, file_path)

    if result == None:
        logging.error(
            f"Could not get the month and year from file: {file_path}")
        exit(1)

    return MonthYear(result.group("month"), result.group("year"))


def get_datetime_from_file_name(file_path):
    """Generates a datetime object using the month and year from the files name"""
    file_month, file_year = get_month_year_from_file(file_path)
    return get_datetime(file_month, file_year)
