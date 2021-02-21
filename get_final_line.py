from collections import deque


def get_final_line(f):
    """ returns the last line of the file f"""
    try:
        with open(f) as f:
            return "".join(deque(f.readlines(), 1))
    except FileNotFoundError:
        print("file not found")


if __name__ == "__main__":
    file_name = input("please enter the file name: ")
    print(get_final_line(file_name))
