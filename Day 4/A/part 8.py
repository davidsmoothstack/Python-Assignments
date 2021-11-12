def even_only(*list):
    return [x for x in list if x % 2 == 0]


print(even_only(1, 2, 3, 4, 5, 6))
