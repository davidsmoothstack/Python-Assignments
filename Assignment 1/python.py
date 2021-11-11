def createTriangle(length):
    starCount = 1

    for i in range(length):
        for space in range(length - starCount):
            print(" ", end = "")

        for star in range(starCount):
            print("*", end = "")

        print()
        starCount = starCount + 1

createTriangle(3)