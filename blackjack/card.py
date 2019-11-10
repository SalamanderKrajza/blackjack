class Card():
    '''
    Class desinged to describe every card object in deck
    '''
    def __init__(self, suit, rank):
        '''
        This method is taking suit and rank of card, and generate its name or value
        INPUT: 
            suit - "color" of card. f.e: 'heart' or 'spade'
            rank - number between 2 and 10 or rank as word f.e 'king', 'queen'
        '''
        self.name = str(rank).capitalize() + " of " + str(suit).capitalize()
        self.suit = suit
        self.rank = rank
        self.visible = True
        self.display = [['']*8]*5
        try:
            self.value = int(rank)
        except ValueError:
            if rank == 'Ace':
                #Ace could be worth 1 or 11. We will start with 1 but user can update it later
                self.value = 1
            else:
                #All Jacks, Queens and Kings are worth 10
                self.value = 10

    def change_ace_value(self, value):
        '''
        Due to fact that player have ability to choose value of ace (as 1 or 11), 
        We will let him do it with this function
        '''
        self.value = value
    
    def display_card(self):
        '''
        This function transforms card names into graphic representation
        '''
        if not self.visible:
            symbol = '???'
        else:
            if self.suit == 'diamond':
                suit_symbol = '♦' 
            elif self.suit == 'heart':
                suit_symbol = '♥' 
            elif self.suit == 'club':
                suit_symbol = '♣' 
            elif self.suit == 'spade':
                suit_symbol = '♠' 
            symbol = str(self.name[0]) + ' ' + suit_symbol

            #if we have card 10 we need to replace empty space betweeen suit symbol and first letter/number of rank
            #So wy change for example '1 ♥' into '10♥' 
            if symbol[0] == '1':
                symbol = str(self.name[0]) + '0' + suit_symbol

        self.display[0]=list('╔═════╗')
        self.display[1]=list('║╔═══╗║')
        self.display[2]=list(f'║║{symbol}║║')
        self.display[3]=list('║╚═══╝║')
        self.display[4]=list('╚═════╝')
        return self.display
        # for x in range(0,5):
        #     print(''.join(self.display[x]))