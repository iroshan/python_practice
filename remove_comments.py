
'''
Python uses the # character to mark the beginning of a comment.
The comment ends at the end of the line containing the # character.
In this exercise, you will create a program that removes all of the comments from a Python source file.
Check each line in the file to determine if a # character is present.
If it is then your program should remove all of the characters from the # character to the end of the line
(we’ll ignore the situation where the comment character occurs inside of a string). Save the modified file using a new name that will be entered by the user.
The user will also enter the name of the input file.
Ensure that an appropriate error message is displayed if a problem is encountered while accessing the files.
'''

import os


def remove_comments():
    try:
        read_file = input("enter the name of the file: ").strip()
        write_file = input("enter the name for new file: ").strip()
        with open(read_file, 'r') as r:
            with open(write_file, 'w') as w:
                for line in r:
                    if line.startswith('#'):
                        continue
                    if '#' in line:
                        line = line[:line.index('#')] + '\n'
                    w.write(line)
                print("comments removal complete.")
    except Exception as e:
        print(
            f"Cannot access the file\n{e}."
            f"Please place the file in {os.getcwd()} or enter full path.")


if __name__ == '__main__':
    remove_comments()
