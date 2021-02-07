def hex_to_decimal(hex_num):
    """ retruns the decimal number for hex_num"""
    decimal_num = 0
    # reverse string
    reversed_hex = reversed(hex_num)
    # for each number of the string, add the corresponding decimal value to decimal_num
    for i, v in enumerate(reversed_hex):
        decimal_num += (16**i) * int(v,16)
    return decimal_num


def main():
    while True:
        hex_input = input("enter hex number to convert to decimal (blank to quit): ")
        if not hex_input:
            print("No input. Qutting...")
            break
        if hex_input.isnumeric():
            decimal_num = hex_to_decimal(hex_input)
            print(f"{hex_input} is equal to decimal number {decimal_num}.")
        else:
            print(f"{hex_input} is not a valid number.")


if __name__ == '__main__':
    main()