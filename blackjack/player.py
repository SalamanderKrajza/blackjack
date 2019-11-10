import os

class Player():
    '''
    Player will have some properties like cards, account balance etc.
    Also, player will have some methods which are responsibile for playing the game
    '''
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.balance = 1000
    
    def bet(self):
        '''
        This function will ask player for his bet
        If player have money, function will reduce his current balance by amount betted 
        If player have not enough money/his input is not valid it will ask player again
        OUTPUT: INT - given_input - amount that is taken from current balance for the bet
        '''
        while True:
            print(f'Dear {self.name}, your current bilans is {self.balance}')
            try:
                given_input = int(input('Please, tell us how much youwant to bet in this turn: '))
            except:
                os.system('cls')
                print(f'{WRONG_INPUT}\nYou have to give us number!\n')
            else:
                os.system('cls')
                if given_input<=0:
                    print(f'{WRONG_INPUT}\nYou have to give give us value above 0!\n')
                    continue
                else:
                    if self.balance >= given_input:
                        self.balance -= given_input
                        print(f'You are betting: {given_input}\nYour current balance is: {self.balance}')
                        return given_input
                    else:
                        print(f'{WRONG_INPUT}\nYour balance is too small for this bet!\n')
                        continue

    def pick_cards(self, somedeck):
        '''
        This function will give player 2 cards from the deck
        '''
        for x in range(0,2):
            self.hit(somedeck)

    # def stand(self):
    #     '''
    #     This is one of possible player actions
    #     '''

    def hit(self, somedeck):
        '''
        This function will give player 1 card from the deck
        '''
        self.cards.append(somedeck.cards.pop(0))

    def make_hidden(self, makehidden=True):
        '''
        This is function for computer player
        It make card hidden for player
        It make card visible for player if (optional argument) makehidden = False
        (Optional)INPUT: True/False value which determines if cards should be hidden or shown
        '''
        if makehidden:
            self.cards[1].visible = False
            self.cards[1].name = "Hidden card"
        else:
            self.cards[1].visible = True
            self.cards[1].name = self.cards[1].name = str(self.cards[1].rank).capitalize() + " of " + str(self.cards[1].suit).capitalize()

    def display_cards(self):
        '''
        This function will show all cards which player have
        '''
        for y in range(0, 5):
            for x in range(0, len(self.cards)):
                print(''.join(self.cards[x].display_card()[y]),end=" ")
            print('')

    def has_ace(self):
        '''
        This function checks if there is any Ace in Player Cards
        OUTPUT: list which contains ID of every ace in player cards
        '''
        result = []
        for x in range(0, len(self.cards)):
            if self.cards[x].rank == 'Ace':
                result.append(x)
        if len(result)>=1:
            return result
        else:
            return False

    def calculate_cards_value(self):
        '''
        This method take every card from player hand and returns sum of their value
        OUTPUT: INT - value of all cards in player hand
        '''
        total_value = 0
        for x in range(0, len(self.cards)):
            total_value += self.cards[x].value
        return total_value

    def discard_hand(self):
        for x in range(0, len(self.cards)):
            self.cards.pop()