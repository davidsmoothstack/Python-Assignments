def upperLower(string):
    charlist = []

    for i in range(len(string)):
        currentChar = string[i]

        if i % 2 == 0:
            charlist.append(currentChar.upper())
        else:
            charlist.append(currentChar.lower())

    return "".join(charlist)


print(upperLower("Hello world"))
