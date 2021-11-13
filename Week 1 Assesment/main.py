import re
from datetime import date, datetime

import pandas as pd
from openpyxl.descriptors.base import DateTime
from openpyxl.reader.excel import ExcelReader
from pandas._libs.tslibs.timestamps import Timestamp
from pandas.core.frame import DataFrame

import logger
from my_types import MonthYear, RollingMoMData, SummaryMoMData

sheet_names = ["Summary Rolling Mom",
               "VOC Rolling MoM",
               "Monthly Verbatim Statements"]

# TODO: Remove after getting input from user
sheet_path = "Week 1 Assesment/in/expedia_report_monthly_january_2018.xlsx"


def get_sheet(file_path, sheet_name):
    with pd.ExcelFile(file_path) as xlsx:
        if sheet_name not in xlsx.sheet_names:
            logger.log_message(f"Failed to load sheet: {sheet_name}")
            exit(1)

        return pd.read_excel(xlsx, sheet_name)


def parse_date(month, year):
    try:
        return datetime.strptime(f"{month} {year}", "%B %Y")
    except:
        logger.log_message("Could not parse date")
        exit(1)


def get_month_year_from_file(file_path) -> MonthYear:
    pattern = ".*_(?P<month>.*)_(?P<year>.*?)\.xlsx"
    result = re.search(pattern, file_path)

    if result == None:
        logger.log_message(
            f"Could not get the month or year from file: {file_path}")
        exit(1)

    return MonthYear(result.group("month"), result.group("year"))


def get_summary_rolling_MoM(file_path):
    # Assume the only month without a year is the latest
    # If more than one month without year throw
    sheet = get_sheet(file_path, "Summary Rolling MoM")
    date_col_name = sheet.keys()[0]
    date_col = sheet[date_col_name]

    fileMonth, fileYear = get_month_year_from_file(file_path)
    fileDate = parse_date(fileMonth, fileYear)

    for i, timestamp in enumerate(date_col):
        try:
            if timestamp.month == fileDate.month and timestamp.year == fileDate.year:
                # Skip the first column and spread the rest int oSummaryMoMData
                return SummaryMoMData(*sheet.iloc[i][1::])
        except:
            continue


def get_VOC_rolling_MoM(file_path):
    sheet = get_sheet(file_path, "VOC Rolling MoM")

    fileMonth, fileYear = get_month_year_from_file(file_path)
    date = parse_date(fileMonth, fileYear)

    # TODO: Make dynamic?
    promoters = sheet[date].get(2)
    passives = sheet[date].get(4)
    dectractors = sheet[date].get(6)

    return RollingMoMData(promoters, passives, dectractors)


# TODO: Get file path from user input
month, year = get_month_year_from_file(sheet_path)

rolling_MoM = get_summary_rolling_MoM(sheet_path)
logger.log_summary_rolling_MoM(rolling_MoM)

voc_rolling_MoM = get_VOC_rolling_MoM(sheet_path)
logger.log_VOC_rolling_MoM(voc_rolling_MoM)
