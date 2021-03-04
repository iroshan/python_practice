def sum_numbers():
    """print the sum of numbers entered as a input.
    ignores invalid inputs"""
    data = input("enter the numbers separated by space: ")
    print(sum(int(i) for i in data.split() if i.isdigit()))

if __name__ == "__main__":
    sum_numbers()
