def strsort_ignorecase(word):
    """returns characters of the word sorted, ignoring case"""
    return ''.join(sorted(word, key=lambda s: ord(s.lower())))


def strsort(word):
    """returns sorted word"""
    return "".join(sorted(word))


def main():
    while True:
        word = input('enter word to sort (blank to exit): ').strip()
        if not word:
            print('no word. exiting...')
            break
        print(strsort(word))


if __name__ == '__main__':
    main()
