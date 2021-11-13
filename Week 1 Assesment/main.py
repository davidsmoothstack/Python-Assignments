from datetime import date
import re
from typing import List
from openpyxl.descriptors.base import DateTime
from openpyxl.reader.excel import ExcelReader
import pandas as pd

import pathlib
from pandas._libs.tslibs.timestamps import Timestamp

from pandas.core.frame import DataFrame

sheet_names = [
    "Summary Rolling Mom",
    "VOC Rolling MoM",
    "Monthly Verbatim Statements"
]

path = "Week 1 Assesment/in/expedia_report_monthly_january_2018.xlsx"


def get_sheet(file_path, sheet_name):
    with pd.ExcelFile(file_path) as xlsx:
        if sheet_name in xlsx.sheet_names:
            return pd.read_excel(xlsx, sheet_name)
        else:
            raise Exception("Invalid sheet name: {input_sheet}")


def cols_to_timestamp(data_frame: DataFrame) -> List[Timestamp]:
    returnList = []
    for data in data_frame:
        try:
            returnList.append(pd.to_datetime(data))
        except:
            continue

    return returnList


def get_summary_rolling_MoM(file_path, month):
    # TODO: Store data_sheets in an object
    sheet = get_sheet(file_path, "Summary Rolling MoM")
    date_col = sheet[sheet.keys()[0]]
    timestamps = cols_to_timestamp(date_col)

    for i, timestamp in enumerate(timestamps):
        # TODO: Remove magic number
        if timestamp.month == 1:
            date_col[i]

    return sheet


get_summary_rolling_MoM(path, "January")

# print(
#     get_summary_rolling_MoM(path, "January")
# )
