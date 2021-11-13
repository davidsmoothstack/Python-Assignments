from collections import namedtuple


RollingMoMData = namedtuple(
    "RollingMoMData", ["promoters", "passives", "dectractors"])

MonthYear = namedtuple("MonthYear", ["month", "year"])
