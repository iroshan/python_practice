def pig_latin(word):
  """ returns a sentence converted to pig latin.
  capital letters, punctuations are not supported"""
  if word[0] in 'aeiou':
    return word+"way"
  else:
    return word[1:]+word[0]+'ay'

def main():
    """main program"""
    while True:
      sentence = input('Enter the sentence to translate to pig latin (blank to quit: ').strip()
      if not sentence:
        print("not a sentence")
        break
      words = [pig_latin(word) for word in sentence.lower().split()]
      print(" ".join(words))
      
if __name__ == "__main__" :
    main()
