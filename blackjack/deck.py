from blackjack.card import Card
import random

class Deck():
    '''
    Deck will cointains all existing cards
    '''

    def __init__(self):
        '''
        This method generate list with 52 elements which will be replaced by cards
        Also, this method is calling generate_cards method to replace numbers witch cards
        '''
        self.cards = list(range(0, 52)) #przygotowujemy listę w której umieścimy karty
        self.generate_cards()

    def generate_cards(self):
        '''
        This method will create card elements
        '''
        x = 0
        for suit in ['diamond', 'heart', 'club', 'spade']:
            for rank in (list(range(2,11))+['Jack', 'Queen', 'King', 'Ace']):
                self.cards[x] = Card(suit, rank)
                x+=1

    def shuffle(self):
        '''
        This method will pick every card from deck (in random order) and create new, shuffled deck.
        The new (shuffled deck) replaces old one
        '''
        tempdeck = []
        for x in range(0, len(self.cards)):
            randomcard = random.randint(0, len(self.cards)-1)
            tempdeck.append(self.cards.pop(randomcard))
        self.cards = tempdeck
        print ('\nDeck has been shuffled!\n')

    def print_deck(self):
        '''
        This is method desinged for testing other methods like shuffle
        It shouldn't be used in final project
        It prints name of every cards in deck
        '''
        for x in range(0, len(self.cards)):
            print(self.cards[x].name)
