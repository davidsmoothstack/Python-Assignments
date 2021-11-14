import logging
import re
from datetime import datetime

import pandas as pd

import logger
from my_types import MonthYear, RollingMoMData, SummaryMoMData

sheet_names = ["Summary Rolling Mom",
               "VOC Rolling MoM",
               "Monthly Verbatim Statements"]

# TODO: Remove after getting input from user
# sheet_path = "Week 1 Assesment/in/expedia_report_monthly_january_2018.xlsx"
sheet_path = "Week 1 Assesment/in/expedia_report_monthly_march_2018.xlsx"


def get_sheet(file_path, sheet_name):
    logging.debug(f"Loading up {file_path} with sheet name {sheet_name}")

    with pd.ExcelFile(file_path) as xlsx:
        if sheet_name not in xlsx.sheet_names:
            logging.error(f"Failed to load sheet: {sheet_name}")
            exit(1)

        return pd.read_excel(xlsx, sheet_name)


def parse_date(month, year):
    try:
        logging.debug(f"parse_date with month: {month} year {year}")
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
            f"Could not get the month or year from file: {file_path}")
        exit(1)

    return MonthYear(result.group("month"), result.group("year"))


def get_summary_rolling_MoM(file_path):
    logging.debug(f"Getting summary from {file_path}")
    # Assume the only month without a year is the latest
    # If more than one month without year throw
    sheet = get_sheet(file_path, "Summary Rolling MoM")
    date_col_name = sheet.keys()[0]
    date_col = sheet[date_col_name]

    fileMonth, fileYear = get_month_year_from_file(file_path)
    fileDate = parse_date(fileMonth, fileYear)

    # TODO: Filter out non timestamps
    for row_index, row_date in enumerate(date_col):
        if row_date.month == fileDate.month and row_date.year == fileDate.year:
            # Skip the first column and spread the rest int oSummaryMoMData
            # TODO: Take in month
            return SummaryMoMData(*sheet.iloc[row_index][1::])

    logging.error("Could not find corresponding month in excel file")
    exit(1)


def get_VOC_rolling_MoM(file_path):
    logging.debug(f"Getting VOC from {file_path}")

    sheet = get_sheet(file_path, "VOC Rolling MoM")

    fileMonth, fileYear = get_month_year_from_file(file_path)
    date = parse_date(fileMonth, fileYear)

    month_col = sheet[date] if date in sheet else sheet[fileMonth.title()]

    # TODO: Make dynamic?
    promoters = month_col.get(2)
    passives = month_col.get(4)
    dectractors = month_col.get(6)

    return RollingMoMData(promoters, passives, dectractors)


# TODO: Get file path from user input
month, year = get_month_year_from_file(sheet_path)

rolling_MoM = get_summary_rolling_MoM(sheet_path)
logger.log_summary_rolling_MoM(rolling_MoM)

voc_rolling_MoM = get_VOC_rolling_MoM(sheet_path)
logger.log_VOC_rolling_MoM(voc_rolling_MoM)
