import logging
import sys
from logging import FileHandler, StreamHandler

import util
from my_types import VOCData, SummaryData

format = "[%(asctime)s] %(message)s"
date_format = "%b %d %Y %X"

logging.basicConfig(
    level=logging.DEBUG,
    format=format,
    datefmt=date_format,
    handlers=[
        FileHandler("logs.txt"),
        StreamHandler(sys.stdout)
    ]
)


def log_summary(data: SummaryData):
    logging.info(
        f"\nCalls Offered {data.calls_offered}\n"
        f"Abandoned After 30s {util.to_percent(data.abandoned_after_30s)}\n"
        f"FCR {util.to_percent(data.fcr)}\n"
        f"DSAT {util.to_percent(data.dsat)}%\n"
        f"CSAT {util.to_percent(data.csat)}\n"
    )


def log_VOC(data: VOCData):
    promoter_score = "good" if data.promoters > 200 else "bad"
    passive_score = "good" if data.passives > 100 else "bad"
    decractor_score = "good" if data.dectractors > 100 else "bad"

    logging.info(
        f"\nPromoters {promoter_score}\n"
        f"Passives {passive_score}\n"
        f"Decractors {decractor_score}\n"
    )
