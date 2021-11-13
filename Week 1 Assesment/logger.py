from datetime import datetime
from my_types import RollingMoMData, SummaryMoMData


def log_message(message):
    formatted_time = datetime.now().strftime("%b-%d-%X")
    print(f"[{formatted_time}] {message}")


def log_summary_rolling_MoM(data: SummaryMoMData):
    log_message(
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

    log_message(
        f"\nPromoters {promoter_score}\n"
        f"Passives {passive_score}\n"
        f"Decractors {decractor_score}\n"
    )
