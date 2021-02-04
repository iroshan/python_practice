from random import randint

def guess_num():
    ''' guess a random number between 0 and 100. while users guess is equal to the number provide clues'''
    num = randint(0,100)
    while True:
        try:
            # get the number and check
            guess = int(input('enter your guess: '))
            if num > guess:
                print('too low')
            elif num < guess:
                print('too high')
            else:
                print('That is correct. You won')
                break
        except Exception as e:
            print('Did you enter a valid number? The number must be between 0 and 100')
    


def main():
    print("Guessing Game\nCan you guess my number?\nIt's between 0 and 100")
    guess_num()

if __name__ == '__main__':
    main()
