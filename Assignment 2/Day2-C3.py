def crowd_test(list):
    if len(list) > 5:
        print("It's a crowd")
    elif len(list) > 2:
        print("The room is crowded")
    elif len(list) > 0:
        print("It's not crowded")
    else:
        print("There's no one here")


names = ["David", "Peter", "John", "Sarah", "Luke"]
crowd_test(names)

names.remove("David")
names.remove("Peter")

crowd_test(names)
