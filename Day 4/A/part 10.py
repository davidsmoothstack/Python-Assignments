def fn(x, y):
    if x % 2 == 0 and y % 2 == 0:
        return "Greater than"

    return "Less than"


print(fn(2, 2))
print(fn(2, 3))
