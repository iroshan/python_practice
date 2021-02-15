from collections import Counter

def most_repeating_word(words):
    """ returns the word with most number of repeating words from a list of words."""
    # initialze an empty string and count
    count = 0
    most_repeating_word = ""
    # for each word
    for word in words:
        # count the letters and find the most common letter
        letter_counts = Counter(word).most_common(1)
        # if repeating letter count is more than count variable,
        # update the most_repeating_word and count with values
        if letter_counts[0][1] > count:
            most_repeating_word = word
            count = letter_counts[0][1]
    return word


if __name__ == "__main__":
    # testing the function
    print('Testing with "this is an elementary test example". ')
    print('must print "elementary"')
    words = "this is an elementary test example".strip().lower().split()
    print(most_repeating_word(words)) # == example

    # another test
    print('\nTesting with "This is another sentence". ')
    print('must print "sentence"')
    words = "This is another sentence".strip().lower().split()
    print(most_repeating_word(words)) # == sentence