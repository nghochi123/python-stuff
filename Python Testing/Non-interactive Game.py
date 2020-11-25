'''
Game of War: Each player draw cards. Higher number win.
If same number, At War. 5 cards out. If no 5 cards lose.
In the next draw, who draws the larger card wins all.
'''
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11,
         'Queen': 12, 'King': 13, 'Ace': 14}


'''
Creating Card Class
'''
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return f'{self.value} of {self.suit}'

'''
Creating Deck Class
'''
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

'''
Creating Player Class
'''
class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    def remove_one(self): #Remove one card
        return self.all_cards.pop(0)
    def add_cards(self,new): #Add card
        if type(new) == type([]):
            self.all_cards.extend(new)
        else:
            self.all_cards.append(new)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

'''
Creates deck and shuffles it.
Then, deals cards to each player.
In each round:
Check for 0 cards in each players' hands
Put down one card from each player and add to pot
If one higher, pot goes to higher player
If same, 'War' declared. 5 cards go into the pot.
Next draw who higher wins the pot.
'''
p1 = Player('p1')
p2 = Player('p2')

new_deck = Deck()
new_deck.shuffle()
for i in range(26):
    p1.add_cards(new_deck.deal())
    p2.add_cards(new_deck.deal())
round_number = 0
game_on = True
while game_on:
    round_number += 1
    print(f'It is round {round_number}')
    if len(p1.all_cards) == 0:
        print("Player 1 is out of cards! Player 2 wins")
        game_on = False
        break
    elif len(p2.all_cards) == 0:
        print("Player 2 is out of cards! Player 1 wins")
        game_on = False
        break
        
        #New round
    player_1_cards = []
    player_1_cards.append(p1.remove_one())
    player_2_cards = []
    player_2_cards.append(p2.remove_one())
    for i in player_1_cards:
        print(f'Player 1 Drew {i}')
    for i in player_2_cards:
        print(f'Player 2 Drew {i}')
    at_war = True
    
    while at_war:
        if player_1_cards[-1].value > player_2_cards[-1].value:
            p1.add_cards(player_1_cards)
            p1.add_cards(player_2_cards)
            print(f'Player 1 wins Round {round_number}')
            at_war = False
        elif player_2_cards[-1].value > player_1_cards[-1].value:
            p2.add_cards(player_1_cards)
            p2.add_cards(player_2_cards)
            print(f'Player 2 wins Round {round_number}')
            at_war = False
        else:
            print('War')
            if len(p1.all_cards) < 5:
                print("Player 1 does not have enough cards! Player 2 wins")
                game_on = False
                at_war = False
            elif len(p1.all_cards) < 5:
                print("Player 1 does not have enough cards! Player 2 wins")
                game_on = False
                at_war = False
            else: 
                for num in range(5):
                    player_1_cards.append(p1.remove_one())
                    player_2_cards.append(p2.remove_one())