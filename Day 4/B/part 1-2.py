book_shop = [
    [34587, "Learning Python, Mark Lutz", 4, 40.95],
    [98762, "Programming Python, Mark Lutz", 5, 56.80],
    [77226, "Head First Python, Paul Barry", 3, 32.95],
    [88112, "Einführung in Python3, Bernd Klein", 3, 24.99]]


def get_tuple(book_shop: book_shop):
    return_list = []

    for book_item in book_shop:
        order_number = book_item[0]
        quantity = book_item[2]
        price_per_item = book_item[3]

        product = quantity * price_per_item

        if product > 100:
            product += 10

        return_list.append((order_number, product))

    return return_list


print(get_tuple(book_shop))
