import re
from datetime import date
from typing import List

import pandas as pd
from openpyxl.descriptors.base import DateTime
from openpyxl.reader.excel import ExcelReader
from pandas._libs.tslibs.timestamps import Timestamp
from pandas.core.frame import DataFrame

import logger

sheet_names = [
    "Summary Rolling Mom",
    "VOC Rolling MoM",
    "Monthly Verbatim Statements"
]

sheet_path = "Week 1 Assesment/in/expedia_report_monthly_january_2018.xlsx"


def get_sheet(file_path, sheet_name):
    with pd.ExcelFile(file_path) as xlsx:
        if sheet_name in xlsx.sheet_names:
            return pd.read_excel(xlsx, sheet_name)
        else:
            raise Exception("Invalid sheet name: {input_sheet}")


# def cols_to_timestamp(data_frame: DataFrame) -> List[Timestamp]:
#     returnList = []
#     for data in data_frame:
#         try:
#             returnList.append(pd.to_datetime(data))
#         except:
#             continue

#     return returnList

def get_month_year_from_file(file_path):
    pattern = ".*_(?P<month>.*)_(?P<year>.*?)\.xlsx"
    result = re.search(pattern, file_path)

    if result == None:
        logger.log_message(
            "Could not get the month or year from file: {file_path}")
        exit(1)

    return (result.group("month"), result.group("year"))


def get_rolling_MoM(file_path, month):
    # TODO: Store data_sheets in an object
    sheet = get_sheet(file_path, "Summary Rolling MoM")
    date_col_name = sheet.keys()[0]
    date_col = sheet[date_col_name]

    # TODO: Clean up
    for i, timestamp in enumerate(date_col):
        try:
            # TODO: Remove magic number
            if timestamp.month == 1:
                return sheet.iloc[i, 1:6]
        except:
            continue

    return sheet


def get_VOC_rolling_MoM(file_path, month):
    sheet = get_sheet(file_path, "VOC Rolling MoM")

    return sheet


# TODO: Get file path from user input
month, year = get_month_year_from_file(sheet_path)

rolling_MoM = get_rolling_MoM(sheet_path, month)
# logger.log_rolling_MoM(rolling_MoM)

voc_rolling_MoM = get_VOC_rolling_MoM(sheet_path, month)
# logger.log_VOC_rolling_MoM(voc_rolling_MoM)
