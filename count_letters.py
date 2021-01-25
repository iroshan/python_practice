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
    common= alpha.most_common(1)
    # printing
    print(f'Analysis of {f.name}')
    print('Letter\tpercentage')
    for k,v in alpha.items():
        print(f'{k}\t{v/count*100: >.2f}')
    print(f'\nMost comman letter in this document is "{common [0][0].upper()}" with {common [0][1]} occurrences.')
    
def main():
    try:
        f = input("Please enter the file name: ")
        letter_count(f)
    except Exception as e:
        print (f"failed to do the letter count. {e}")
        
if __name__ == "__main__":
    main()
