'''
Unix-based operating systems usually include a tool named head. 
It displays the first 10 lines of a file whose name is provided as a command line parameter. 
Write a Python program that provides the same behavior. 
Display an appropriate error message if the file requested by the user does not exist or if the command line parameter is omitted.
'''

import sys

if len(sys.argv) != 2:
    sys.exit("Please privide the file name as argument")


try:
    with open(sys.argv[1], 'r') as f:
        for i in range(10):
            print(f.readline().strip())
except FileNotFoundError:
    sys.exit("File not found")
except:
    print("unknown error occured.")
