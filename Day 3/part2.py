def CelsiusToFarenheit(celsius):
    return celsius / 5 * 9 + 32


def FarenheitToCelsius(farenheit):
    return ((farenheit - 32) / 9) * 5


print(CelsiusToFarenheit(60))
print(FarenheitToCelsius(45))
