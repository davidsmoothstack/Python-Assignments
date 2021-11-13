from my_types import RollingMoMData, SummaryMoMData


def log_message(message):
    print(message)


def log_summary_rolling_MoM(data: SummaryMoMData):
    print(
        f"Calls Offered {data.calls_offered}\n"
        f"Abandoned After 30s {data.abandoned_after_30s}\n"
        f"FCR {data.fcr}\n"
        f"DSAT {data.dsat}\n"
        f"CSAT {data.csat}"
    )


def log_VOC_rolling_MoM(data: RollingMoMData):
    promoter_score = "good" if data.promoters > 200 else "bad"
    passive_score = "good" if data.passives > 100 else "bad"
    decractor_score = "good" if data.dectractors > 100 else "bad"

    print(
        f"Promoters {promoter_score}\n"
        f"Passives {passive_score}\n"
        f"Decractors {decractor_score}"
    )
