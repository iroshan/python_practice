from random import sample

# word genearator for testing
s = '''
    This module implements pseudo-random number generators for various distributions.

For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.

On the real line, there are functions to compute uniform, normal (Gaussian), lognormal, negative exponential, gamma, and beta distributions. For generating distributions of angles, the von Mises distribution is available.

Almost all module functions depend on the basic function random(), which generates a random float uniformly in the semi-open range [0.0, 1.0). Python uses the Mersenne Twister as the core generator. It produces 53-bit precision floats and has a period of 2**19937-1. The underlying implementation in C is both fast and threadsafe. The Mersenne Twister is one of the most extensively tested random number generators in existence. However, being completely deterministic, it is not suitable for all purposes, and is completely unsuitable for cryptographic purposes.

The functions supplied by this module are actually bound methods of a hidden instance of the random.Random class. You can instantiate your own instances of Random to get generators that don’t share state.

Class Random can also be subclassed if you want to use a different basic generator of your own devising: in that case, override the random(), seed(), getstate(), and setstate() methods. Optionally, a new generator can supply a getrandbits() method — this allows randrange() to produce selections over an arbitrarily large range.
'''
s = s.strip()

with open('word_list.txt', 'w') as f:
    for word in s.split():
        word = ''.join(filter(str.isalpha, word))
        f.write(word+'\n')

# ---------------------------------------------------------------
# real code


def random_password(f='word_list.txt'):
    with open(f) as f:
        word_list = f.readlines()

    while True:
        password = ''
        word1, word2 = sample(word_list, 2)
        word1, word2 = word1.strip(), word2.strip()
        if len(word1) >= 3 and len(word2) >= 3:
            password = word1.title()+word2.title()
        if (len(password) >= 8) and (len(password) <= 10):
            break

    print(f'the password generated is {password}')


def main():
    print('''
    Random Password Generator\n
    Please enter the file name to take out words.
    or press enter to generate password from default word list file.\n)
    ''')
    f = input("file name: ").strip()
    if f:
        random_password(f)
    else:
        random_password()


main()
