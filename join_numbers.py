def join_numbers(n: int) -> str:
    """returns the numbers from 0 to n as a string"""
    return ",".join([str(i) for i in range(n+1)])


if __name__ == "__main__":
    print("Testing function")
    print(join_numbers(5))
    print(join_numbers(1))
    print(join_numbers(0))
    print(type(join_numbers(5)))
