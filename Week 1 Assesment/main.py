import logging
import sys
import traceback
from datetime import datetime

import logger
import util
from my_types import SummaryData, VOCData


def get_summary_data(file_path):
    logging.debug(f"Parsing summary from {file_path}")

    sheet = util.get_sheet(file_path, "Summary Rolling MoM")

    # Get the name of the first unnamed column
    date_col_name = sheet.keys()[0]
    date_col = sheet[date_col_name]

    file_date = util.get_datetime_from_file_name(file_path)

    for row_index, row_date in enumerate(date_col):
        if (row_date.month, row_date.year) == (file_date.month, file_date.year):
            # Iterate through row data then store in a SummaryData named tuple
            return SummaryData(*sheet.iloc[row_index][0::])

    logging.error("Could not find corresponding month in excel file")
    exit(1)


def get_VOC_data(file_path):
    logging.debug(f"Parsing VOC from {file_path}")

    sheet = util.get_sheet(file_path, "VOC Rolling MoM")

    fileMonth, fileYear = util.get_month_year_from_file_name(file_path)
    col_date = util.get_datetime(fileMonth, fileYear)

    # Use the month string from file if the date column does not exist
    month_col = sheet[col_date] if col_date in sheet else sheet[fileMonth.title()]

    promoters = month_col.get(2)
    passives = month_col.get(4)
    dectractors = month_col.get(6)

    return VOCData(col_date, promoters, passives, dectractors)


if __name__ == "__main__":
    try:
        sheet_path = util.get_console_input()

        summary_data = get_summary_data(sheet_path)
        voc_data = get_VOC_data(sheet_path)

        logger.log_summary_data(summary_data)
        logger.log_VOC_data(voc_data)
    except Exception as e:
        logging.critical(traceback.format_exception_only(type(e), e))
