from collections import namedtuple


RollingMoMData = namedtuple(
    "RollingMoMData", ["promoters", "passives", "dectractors"])

SummaryMoMData = namedtuple(
    "SummaryMoMData",
    ["calls_offered",
     "abandoned_after_30s",
     "fcr",
     "dsat",
     "csat"]
)

MonthYear = namedtuple("MonthYear", ["month", "year"])
