def crowd_test(list):
    if len(list) > 3:
        print("The room is crowded")


names = ["David", "Peter", "John", "Sarah"]
crowd_test(names)

names.remove("David")
names.remove("Peter")

crowd_test(names)
