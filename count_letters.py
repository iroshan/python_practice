import string
from collections import Counter

def letter_count(f):
    # create the dictionary with count zero
    alpha = Counter({k:0 for k in string.ascii_lowercase})
    # keep the count of letters
    count= 0
    with open(f) as f:
        # reading word by word
        for word in f.read():
            # if letter is an alphabet add update the count
            for c in word.lower():
                if c in alpha:
                    alpha[c] += 1
                    count += 1
    # printing
    print(f'Analysis of {f}')
    print('Letter\tpercentage')
    for k,v in alpha.items():
        print(f'{k}\t{v/count*100:.2f}')
    print(f'\n...Most comman letter in this document is {alpha.most_common(1)}...')
        
letter_count('gatsby.txt')