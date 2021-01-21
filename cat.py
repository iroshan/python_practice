'''
Unix-based operating systems typically include a tool named cat, which is short for concatenate.
 Its purpose is to concatenate and display one or more files whose names are provided as command line parameters. 
 The files are displayed in the same order that they appear on the command line.

Create a Python program that performs this task. 
It should generate an appropriate error message for any file that cannot be displayed, and then proceed to the next file. 
Display an appropriate error message if your program is started without any command line parameters.not''
'''
import sys

if len(sys.argv) < 2:
	sys.exit("Please privide the file name(s) as argument(s)")


for arg in sys.argv[1:]:
    try:
        with open(arg, 'r') as f:
            for line in f.readlines():
                print(line)
    except Exception as e:
        print(f"Cannot process {arg}. {e}")
        continue