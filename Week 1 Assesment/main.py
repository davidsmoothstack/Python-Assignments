import logging
import sys
from datetime import datetime

import logger
import util
from my_types import VOCData, SummaryData

sheet_names = ["Summary Rolling Mom",
               "VOC Rolling MoM",
               "Monthly Verbatim Statements"]


def get_summary(file_path):
    logging.debug(f"Parsing summary from {file_path}")

    sheet = util.get_sheet(file_path, "Summary Rolling MoM")

    # Get the name of the first unnamed column
    date_col_name = sheet.keys()[0]
    date_col = sheet[date_col_name]

    file_date = util.get_date_from_file_name(file_path)

    # TODO: Filter out non timestamps
    for row_index, row_date in enumerate(date_col):
        if row_date.month == file_date.month and row_date.year == file_date.year:
            # Skip the first column and spread the rest int oSummaryMoMData
            # TODO: Take in month
            return SummaryData(*sheet.iloc[row_index][1::])

    logging.error("Could not find corresponding month in excel file")
    exit(1)


def get_VOC(file_path):
    logging.debug(f"Parsing VOC from {file_path}")

    sheet = util.get_sheet(file_path, "VOC Rolling MoM")

    fileMonth, fileYear = util.get_month_year_from_file(file_path)
    col_date = util.parse_date(fileMonth, fileYear)

    # Use the month string from file if the date column does not exist
    month_col = sheet[col_date] if col_date in sheet else sheet[fileMonth.title()]

    promoters = month_col.get(2)
    passives = month_col.get(4)
    dectractors = month_col.get(6)

    return VOCData(promoters, passives, dectractors)


if __name__ == "__main__":
    try:
        sheet_path = util.get_console_input()

        summary_data = get_summary(sheet_path)
        logger.log_summary(summary_data)

        voc_data = get_VOC(sheet_path)
        logger.log_VOC(voc_data)
    except:
        e = sys.exc_info()[0]
        logging.error(e.__name__)
