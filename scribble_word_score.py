# Create the dictionary
letter_scores = {}
for c in "aeilnorstu":
    letter_scores[c] = 1
for c in "dg":
    letter_scores[c]=2
for c in "bcmp":
    letter_scores[c]=3
for c in "fhvwy":
    letter_scores[c]=4
letter_scores['k']=5
for c in "jx":
    letter_scores[c]=8
for c in "qz":
    letter_scores[c]=10
    

# function to get word score
def get_word_score(word):
    '''
    return the score for the word according the letter scores
    '''
    return sum([letter_scores[k] for k in word.lower()])
    # @gocher, Why isn't this working? thx. 
    # managed to fix it. Still indentation is a mess. 
    # using the phone. 

    # return score
   # score=0
   # for c in word.lower():
   #     score += letter_scores[c]
   # return score

# main program
while True:
    word = input("Please enter the scrabble word: ").strip()
    if not word:
        print("No word entered. Exiting...")
        break
    elif not word.isalpha():
        print('only letters allowed. Try again... \n ')
        continue
    else:
        score = get_word_score(word)
        print(f"The word '{word}' has a score of {score} \n")
