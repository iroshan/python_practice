def recursive_sum(n=0):
    ''' recursively add the input to n and print the total when the input is blank'''
    try:
        i = input('enter a number: ')
        # base case
        if not i:
            print(f'total = {n}')
        # check if a number
        elif not i.isnumeric():
            print("not a number")
            recursive_sum(n)
        # add the number and do recursion
        else:
            recursive_sum(int(i)+n)
    except Exception as e:
        print(e)


def main():
    print("SUM OF NUMBERS")
    recursive_sum()

if __name__ == '__main__':
    main()