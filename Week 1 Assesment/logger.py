import logging
import sys
from datetime import date, datetime
from logging import FileHandler, Formatter, Logger, StreamHandler

from my_types import RollingMoMData, SummaryMoMData

format = "[%(asctime)s] %(message)s %(message)s"
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


def log_summary_rolling_MoM(data: SummaryMoMData):
    # TODO: Show percents
    logging.info(
        f"\nCalls Offered {data.calls_offered}\n"
        f"Abandoned After 30s {data.abandoned_after_30s}\n"
        f"FCR {data.fcr}\n"
        f"DSAT {data.dsat}\n"
        f"CSAT {data.csat}\n"
    )


def log_VOC_rolling_MoM(data: RollingMoMData):
    promoter_score = "good" if data.promoters > 200 else "bad"
    passive_score = "good" if data.passives > 100 else "bad"
    decractor_score = "good" if data.dectractors > 100 else "bad"

    logging.info(
        f"\nPromoters {promoter_score}\n"
        f"Passives {passive_score}\n"
        f"Decractors {decractor_score}\n"
    )
