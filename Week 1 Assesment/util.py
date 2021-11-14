import logging
import pathlib
import re
import sys
from datetime import datetime

from my_types import MonthYear


def percent_format(float):
    return "{:.2%}".format(float)


def comma_format(number):
    return "{:,.0f}".format(number)


def get_console_input():
    args = sys.argv

    if len(args) != 2:
        logging.error("Incorrect amount of arguments")
        exit(1)

    if not pathlib.Path(args[1]).is_file:
        logging.error(f"File does not exist: {args[1]}")
        exit(1)

    return args[1]


def get_datetime(month, year):
    """Returns a datetime object from the provided month and year"""
    try:
        logging.debug(f"parse_date with month: \"{month}\" year: \"{year}\"")
        return datetime.strptime(f"{month} {year}", "%B %Y")
    except:
        logging.error("Could not parse date")
        exit(1)


def get_file_monthyear(file_path) -> MonthYear:
    """Returns a MonthYear tuple with a month and a year using the provided file name"""
    logging.debug(f"Reading month and year from {file_path}")
    pattern = ".*_(?P<month>.*)_(?P<year>.*?)\.xlsx"
    result = re.search(pattern, file_path)

    if result == None:
        logging.error(
            f"Could not get the month and year from file: {file_path}")
        exit(1)

    return MonthYear(result.group("month"), result.group("year"))


def get_file_datetime(file_path):
    """Returns a datetime object using the month and year from the provided file name"""
    file_month, file_year = get_file_monthyear(file_path)
    return get_datetime(file_month, file_year)
