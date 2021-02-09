import string
from collections import Counter
from decorators import timer, debug

@timer
@debug
def letter_count(f):
    # create the dictionary with count zero
    alpha = Counter({k:0 for k in string.ascii_lowercase})
    # keep the count of letters
    count= 0
    with open(f) as f:
        # reading word by word
        for word in f.read():
            
            letters = set(word.lower())
            # if letter is an alphabet add update the count
            for c in letters:
                if c in alpha:
                    alpha[c] += 1
                    count += 1
    least_common= alpha.most_common()[-1]
    #sorted_v = sorted([v,k for k,v in alpha.items()])
    # printing
    print(f'Analysis of {f.name}')
    print('Letter\tpercentage')
    for k,v in alpha.items():
        print(f'{k}\t{v/count*100: >.2f}')
    print(f'\nLeast comman letter in this document is "{least_common[0]}" with {least_common[1]} occurrences.')
    
def main():
    try:
        f = input("Please enter the file name: ")
        letter_count(f)
    except Exception as e:
        print (f"failed to do the letter count. {e}")
        
if __name__ == "__main__":
    main()
