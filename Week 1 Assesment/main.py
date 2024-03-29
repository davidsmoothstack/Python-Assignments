import logging

import pandas as pd

import logger
import util
from my_types import SummaryData, VOCData


def get_sheet(excel_path, sheet_name):
    """Returns an excel sheet in the form of a list of DataFrames from the specified excel path"""
    logging.debug(f"Loading up {excel_path} with sheet name {sheet_name}")

    with pd.ExcelFile(excel_path) as xlsx:
        if sheet_name not in xlsx.sheet_names:
            logging.error(f"Failed to load sheet: {sheet_name}")
            exit(1)

        return pd.read_excel(xlsx, sheet_name)


def get_summary_data(excel_path):
    """Returns a SummaryData named tuple that contains data from the "Summary Rolling MoM" sheet

    This function determines the column to read from based on the month and year located in the file name
    """
    logging.debug(f"Parsing summary from {excel_path}")

    excel = get_sheet(excel_path, "Summary Rolling MoM")

    # sheet.keys()[0] Gets a reference to the first unnamed column
    date_col = excel[excel.keys()[0]]
    file_date = util.get_file_datetime(excel_path)

    for row_index, row_date in enumerate(date_col):
        if (row_date.month, row_date.year) == (file_date.month, file_date.year):
            # Get all the values in the row
            row_data = list(excel.iloc[row_index])
            return SummaryData(*row_data)

    logging.error("Could not find corresponding month in excel file")
    exit(1)


def get_VOC_data(excel_path):
    """Returns a VOCData named tuple that contains data from the "VOC Rolling MoM" sheet

    This function determines the column to read from based on the month and year located in the file name
    """
    logging.debug(f"Parsing VOC from {excel_path}")

    fileMonth, fileYear = util.get_file_monthyear(excel_path)
    col_date = util.get_datetime(fileMonth, fileYear)

    excel = get_sheet(excel_path, "VOC Rolling MoM")

    # Use the month string from file if the date column does not exist
    target_col = excel[col_date] if col_date in excel else excel[fileMonth.title()]

    promoters = target_col.get(2)
    passives = target_col.get(4)
    dectractors = target_col.get(6)

    return VOCData(col_date, promoters, passives, dectractors)


if __name__ == "__main__":
    try:
        excel_path = util.get_console_input()

        summary_data = get_summary_data(excel_path)
        voc_data = get_VOC_data(excel_path)

        logger.log_summary_data(summary_data)
        logger.log_VOC_data(voc_data)
    except:
        logging.exception("")
