'''
Initialising the necessary variables
'''

import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
         'Queen': 10, 'King': 10, 'Ace': 11}

#Card Class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return f'{self.rank} of {self.suit}'

#Deck class with shuffle and deal methods
class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank)) #Calling deck creates a Deck with 52 Cards
    def shuffle(self): #Shuffle Deck
        random.shuffle(self.all_cards)
    def deal(self): #Deal cards (one)
        return self.all_cards.pop()

#Player class with 
class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    def add_cards(self,new): #Add card
        self.all_cards.append(new)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


game_on = True
for i in range(3):
    p1 = Player('p1') 
    p2 = Player('p2')
    print('Shuffling...')
    new_deck = Deck()
    new_deck.shuffle()
    print('Dealing...')
    for i in range(2):
        p1.add_cards(new_deck.deal())
        p2.add_cards(new_deck.deal())
    score1 = 0
    score2 = 0
    print('Your cards are: ')
    for i in p1.all_cards:
        score1 += i.value
        print(i)
    print(f'Your score is {score1}')
    decision = ''
    while decision != 'n':
        decision = input('Would you like another card? y/n')
        if decision == 'y':
            p1.add_cards(new_deck.deal())
            score1 = 0
            for i in p1.all_cards:
                score1 += i.value
                print(i)
            print(f'Your score is {score1}')
    print('Show Hand!')
    for i in p2.all_cards:
        score2 += i.value
        print(i)
    print(f'Player 2 has {score2} points!')
    if score2 > score1:
        print('Player 2 wins!\n')
    elif score2 < score1:
        print('Player 1 wins!\n')
    else:
        print('It is a draw\n')