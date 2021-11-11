def crowd_test(list):
    if len(list) > 3:
        print("The room is crowded")
    else:
        print("It's not very crowded")


names = ["David", "Peter", "John", "Sarah"]
crowd_test(names)

names.remove("David")
names.remove("Peter")

crowd_test(names)
