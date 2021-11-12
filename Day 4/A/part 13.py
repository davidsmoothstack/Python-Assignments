def fun(string):
    char_list = []

    for i in range(len(string)):
        char = string[i]

        if i == 0 or i == 2:
            char_list.append(char.upper())
        else:
            char_list.append(char)

    return "".join(char_list)


print(fun("Hello world"))
