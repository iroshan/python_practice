menu = {'sandwitch': 10, 'tea': 7, 'cofee': 8, 'bun': 4, 'hotdog': 12}


def restaurant():
    """take orders and print the return value on blank input"""
    total = 0  # to keep the total price
    while True:
        item = input('Order: ').lower().strip()
        if not item:
            # break the loop if order is empty and print total
            print(f'Your total is {total}.')
            break
        if item in menu:
            # if item in the menu, print the item and add the price to total
            total += menu[item]
            print(f'{item} costs {menu[item]}. Total is {total}.')
        else:
            # if item is not in the menu
            print(f'We are fresh out of {item} today.')


if __name__ == '__main__':
    """main program"""
    restaurant()
