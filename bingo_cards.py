import random

# create the card dictionary
bingo_cards={}
n=1
for c in 'BINGO':
  bingo_cards[c] =[i for i in range(n,n+15)]
  n +=15
 
 
# function to create and print a random bingo card
def print_card():
	print(*bingo_cards.keys(),sep='\t')
	for _ in range(5):
		card = {k:(random.choice(bingo_cards[k])) for k in bingo_cards.keys()}
		print(*card.values(),sep='\t')


if __name__ == '__main__':
	print_card()


