import random

suits = ('H', 'D', 'C', 'S')
faces = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
card_power = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}


class Card(object):

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __str__(self):
        return '{}{}'.format(self.face, self.suit)

    def get_power(self):
        return card_power[self.face]


class Player(object):

    def __init__(self, cash=100):
        self.cash = cash

    def increase_cash(self, amount):
        self.cash += amount

    def decrease_cash(self, amount):
        if amount >= self.cash:
            self.cash = 0
            print 'You lost it all!'
        else:
            self.cash -= amount


class Dealer(object):

    def __init__(self, deck):
        self.deck = deck
        pass


class Deck(object):
    '''
    Create a deck of cards from all possible faces and suits
    Also shuffle on initialization
    '''

    def __init__(self):
        self.deck = []

        for suit in suits:
            for face in faces:
                self.deck.append(Card(face, suit))
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


game_deck = Deck()
for card in game_deck.deck:
    print "Card: {} with power {}".format(card, card.get_power())
