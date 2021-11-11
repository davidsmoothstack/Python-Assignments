def createTriangle(peakHeight):
    for i in range(peakHeight + 1):
        print("*" * i)

    for i in reversed(range(peakHeight)):
        print("*" * i)


createTriangle(5)
