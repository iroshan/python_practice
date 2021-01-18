#!/usr/bin/python

import random

# create the card dictionary

bingo_cards = {}
n = 1
for c in 'BINGO':
bingo_cards[c] = [i for i in range(n, n + 15)]
n += 15

#function to createa random bingo card
def create_card():
card = {
	k: (random.sample(bingo_cards[k], 5)) for k in bingo_cards.keys()}
return card


# print the card
def print_card(card):
print(* bingo_cards.keys(), sep = '\t')
transpose = zip(* card.values())
for row in transpose:
print(* row, sep = '\t')


if __name__ == '__main__':
print_card(create_card())