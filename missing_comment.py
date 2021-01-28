'''
Coding Challenge: Day 43: Missing Comments
'''

import sys

# search a file for functions without a comment before and print the line numbers and the function names.
def missing_comments(f):
    try:
        with open(f, 'r') as f:
            lines = f.readlines()
            found = 0
            missing = 0
            for i,line in enumerate(lines):
                if line.startswith('def '):
                    found += 1
                    if not lines[i-1].startswith('#'):
                        missing += 1
                        # func = re.search('def\ (\S+)\:',line)[0]\
                        func = line.partition("def ")[2].partition(":")[0]
                        print(f'Missing comment in {f.name} on line {i-1} for the function "{func}"')
            if found and not missing:
                print(f'Great! \nAll {found} functions in {f.name} are commented.')
            if not found:
                print('no functions were detected')
    except Exception as e:
        print(e)



def main():
    try:
        if len(sys.argv)>1:
            for arg in sys.argv[1:]:
                missing_comments(arg)
        else:
            file_name = input("Enter the file name to check for missing comments: ")
            missing_comments(file_name)
    except Exception as e:
        print(f'Error occured! \n {e}')

if __name__ == '__main__':
    main()