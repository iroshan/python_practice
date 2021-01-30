def palindrome_check(word):
    ''' return True if 'word' is palindrome'''
    # base case
    if len(word) <= 1:
        return True
    # check first and last letters.
    if word[0] != word[-1]:
        return False
    #recursively check each letter
    return palindrome_check(word[1:-1])



def main():
    print('Palindrome checker\nEnter the word to check for palindrome. Enter blank to exit\n')
    while True:
        word = input("please enter word: ").strip().lower()
        if word:
            if palindrome_check(word):
                print(f'"{word}" is a palindrome.')
            else:
                print(f'"{word}" is NOT a palindrome.')
        else:
            print("No word entered. exiting...")
            break


if __name__ == '__main__':
    main()