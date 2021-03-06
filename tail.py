'''
Unix-based operating systems also typically include a tool named tail. 
It displays the last 10 lines of a file whose name is provided as a command line parameter. 
Write a Python program that provides the same behavior. 
Display an appropriate error message if the file requested by the user does not exist or if the command line parameter is omitted...

'''

import sys
from collections import deque

if len(sys.argv) != 2:
    sys.exit("Please privide the file name as argument")


try:
    with open(sys.argv[1], 'r') as f:
    	 print("\n".join(deque( f,10)))
except FileNotFoundError:
    sys.exit("File not found")
except:
    print("unknown error occured.")
