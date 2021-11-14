from collections import namedtuple


VOCData = namedtuple(
    "VOCData", ["promoters", "passives", "dectractors"])

SummaryData = namedtuple(
    "SummaryData",
    ["date",
     "calls_offered",
     "abandoned_after_30s",
     "fcr",
     "dsat",
     "csat"]
)

MonthYear = namedtuple("MonthYear", ["month", "year"])
