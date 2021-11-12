def calculate_bmi(weightKg, heightMeters):
    bmi = weightKg / (heightMeters) ** 2

    if bmi < 18.5:
        return "under"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "over"
    else:
        return "obese"


input = [
    "3",
    "80 1.73",
    "55 1.58",
    "49 1.91"
]

input_length = int(input[0])

for i in range(1, input_length + 1):
    string = input[i].split(" ")
    weight, height = map(lambda x: float(x), tuple(string))
    print(calculate_bmi(weight, height))
