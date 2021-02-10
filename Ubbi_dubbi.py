def translate(word):
  s= ['ub'+c if c in 'aeiou' else c for c in word ]
  return ''.join(s)
  
  
def main():
  while True:
    word = input('enter word: ').strip().lower()
    if not word:
      print('no word. exiting...')
      break
    print(translate(word))
    
    
if __name__ == '__main__':
  main()
