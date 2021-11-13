from my_types import RollingMoMData


def log_message(message):
    print(message)


def log_summary_rolling_MoM(data):
    print(data)


def log_VOC_rolling_MoM(data: RollingMoMData):
    promoter_score = "good" if data.promoters > 200 else "bad"
    passive_score = "good" if data.passives > 100 else "bad"
    decractor_score = "good" if data.dectractors > 100 else "bad"

    print(
        f"Promoters {promoter_score}\n"
        f"Passives {passive_score}\n"
        f"Decractors {decractor_score}"
    )
