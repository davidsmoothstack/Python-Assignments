from typing import Type


datalist = [1452, 11.23, 1+2j, True, 'w3resource',
            (0, -1), [5, 12], {"class": 'V', "section": 'A'}]

for obj in datalist:
    print(type(obj), obj)
