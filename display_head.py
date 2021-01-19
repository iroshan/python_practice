"""
Unix-based operating systems usually include a tool named head. It displays the first 10 lines of a file whose name is provided as a command line parameter. Write a Python program that provides the same behavior. Display an appropriate error message if the file requested by the user does not exist or if the command line parameter is omitted.
"""
import os


def display_head(file):
    try:
        with open(file, "r") as f:
            for i in range(10):
                print(f.readline())
    except FileNotFoundError:
        print(
            f"File not found. \nPlease place the file in {os.getcwd()} or enter the full path and try again."
        )


def main():
    file = input("please enter file name to display first 10 lines: ").strip()
    if not file:
    	print(f"No file name entered.\nPlease place the file in {os.getcwd()} or enter the full path and try again.")
    else:
    	display_head(file)


main()
