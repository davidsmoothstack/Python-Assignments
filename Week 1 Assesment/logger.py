import logging
import sys
from datetime import datetime
from logging import FileHandler, StreamHandler

from util import comma_format, percent_format
from my_types import SummaryData, VOCData

logging_format = "[%(asctime)s] %(message)s"
logging_date_format = "%b %d %Y %X"

logging.basicConfig(
    level=logging.DEBUG,
    format=logging_format,
    datefmt=logging_date_format,
    handlers=[
        FileHandler("logs.txt"),
        StreamHandler(sys.stdout)
    ]
)


def log_summary_data(data: SummaryData):
    logging.info(
        f"Summary for {data.date.strftime('%B %Y')}: \n"
        f"Calls Offered: {comma_format(data.calls_offered)}\n"
        f"Abandoned After: {percent_format(data.abandoned_after_30s)}\n"
        f"FCR: {percent_format(data.fcr)}\n"
        f"DSAT: {percent_format(data.dsat)}\n"
        f"CSAT: {percent_format(data.csat)}\n"
    )


def log_VOC_data(data: VOCData):
    promoter_score = "good" if data.promoters > 200 else "bad"
    passive_score = "good" if data.passives > 100 else "bad"
    decractor_score = "good" if data.dectractors > 100 else "bad"

    logging.info(
        f"VOC for {data.date.strftime('%B %Y')}\n"
        f"Promoters {promoter_score} ({comma_format(data.promoters)})\n"
        f"Passives {passive_score} ({comma_format(data.passives)})\n"
        f"Decractors {decractor_score} ({comma_format(data.dectractors)})\n"
    )
