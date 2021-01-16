def anagram(x, y):
  if len(x) != len(y):
  	return False
  dic1= dict(enumerate(x))
  dic2= dict(enumerate(y))
  for i in range(len(x)):
    if dic1[i] != dic2[len(x)-1-i]:
      return False
  return True

x,y = input("please enter two words seperated by space: ").strip().split()
if anagram(x,y):
	print(f"Awesome!... {x} and {y} are are anagrams")
else:
	print(f"Nope. {x} and {y} are not anagrams")