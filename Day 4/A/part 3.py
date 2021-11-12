def func3(x, y, z):
    if z:
        return x
    return y


print(func3("hello", "goodbye", False))
print(func3("hello", "goodbye", True))
