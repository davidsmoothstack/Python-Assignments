book_shop = [
    [34597, ("Learning Python, Mark Lutz", 4, 40.95)],
    [98762, ("Programming Python, Mark Lutz", 5, 56.80)],
    [77226, ("HeadFirst Python, Paul Barry", 3, 32.95)],
    [88112, ("Einfuhrung in Python3, Bernd Klein", 3, 24.99)]]


def get_tuple(book_shop):
    return_list = []
    for book_item in book_shop:
        order_number = book_item[0]
        _, quantity, price_per_item = book_item[1]
        total = quantity * price_per_item

        return_list.append((order_number, total))

    return return_list


print(get_tuple(book_shop))
