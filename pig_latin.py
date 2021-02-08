def pig_latin(word):
    """translate the word to pig latin"""
    if word[0] in 'aeiou':
        return word+"way"
    else:
        return word[1:]+word[0]+'ay'


while True:
    word = input(
        'Enter the word to ranslate to pig latin: (blank to exit) ').strip().lower()
    if word:
        print(pig_latin(word))
    else:
        print('exiting...')
        break
