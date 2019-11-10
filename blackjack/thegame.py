COMPUTER_HAND = ("\n\n░▐█▀█▒▐█▀▀█▌▒▐██▄▒▄██▌▒▐█▀█▒█▒█▒█▀█▀█░▐█▀▀▒▐█▀▀▄     ░▐█░▐█─░▄█▀▄─▒██▄░▒█▌░▐█▀█▄\n\
░▐█──▒▐█▄▒█▌░▒█░▒█░▒█░▒▐█▄█▒█▒█░░▒█░░░▐█▀▀▒▐█▒▐█     ░▐████░▐█▄▄▐█▒▐█▒█▒█░░▐█▌▐█\n\
░▐█▄█▒▐██▄█▌▒▐█░░░░▒█▌▒▐█░░▒▀▄▀░▒▄█▄░░▐█▄▄▒▐█▀▄▄     ░▐█░▐█░▐█─░▐█▒██░▒██▌░▐█▄█▀")
PLAYER_HAND = ("\n\n▒▐█▀█▒██░░░─░▄█▀▄─▒▀▄░░░░░▄▀░▐█▀▀▒▐█▀▀▄     ░▐█░▐█─░▄█▀▄─▒██▄░▒█▌░▐█▀█▄\n\
▒▐█▄█▒██░░░░▐█▄▄▐█░░▒▀▄░▄▀░░░▐█▀▀▒▐█▒▐█     ░▐████░▐█▄▄▐█▒▐█▒█▒█░░▐█▌▐█\n\
▒▐█░░▒██▄▄█░▐█─░▐█░░░░▒█░░░░░▐█▄▄▒▐█▀▄▄     ░▐█░▐█░▐█─░▐█▒██░▒██▌░▐█▄█▀")
WRONG_INPUT = "\n█░░░█ █▀▀▄ ▄▀▄ █▄░█ ▄▀▀░     ▀ █▄░█ █▀▄ █░█ ▀█▀ \n█░█░█ █▐█▀ █░█ █░▀█ █░▀▌     █ █░▀█ █░█ █░█ ░█░ \n░▀░▀░ ▀░▀▀ ░▀░ ▀░░▀ ▀▀▀░     ▀ ▀░░▀ █▀░ ░▀░ ░▀░ \n"

class TheGame():
    '''
    Class with methods like check_win_conditions etc
    '''
    def __init__(self):
        self.is_going = True
        self.turn = 'Player1'

    def current_board(self, player1, player2):
        '''
        Displays current state of the game
        '''
        print(COMPUTER_HAND)
        player2.display_cards()
        for x in range(0, len(player2.cards)):
            print(player2.cards[x].name)

        print(PLAYER_HAND)
        player1.display_cards()
        for x in range(0, len(player1.cards)):
            print(player1.cards[x].name)

    def player_turn(self, mydeck, player1, player2):
        '''
        This method dispalys current board state and ask player for his move
        INPUT: mydeck as Deck object, player1 and player2 as Player objects
        '''
        while player1.calculate_cards_value()<21:
            self.current_board(player1, player2)
            given_input = input('Player1, you can [hit] or [stand], what do you prefer?: ')
            if given_input == 'hit':
                player1.hit(mydeck)
                continue
            elif given_input == 'stand':
                print()
                break
            else:
                print(WRONG_INPUT)
                input("Press ENTER to continue ")
                continue

        #check if player have ace and ask for its value
        p1_has_ace = player1.has_ace()
        if p1_has_ace:
            for x in range (0, len(p1_has_ace)):
                print(f'You have at least 1 Ace in your hand\nPlease, choose value 1 or 11 card number {p1_has_ace[x]+1}')
                while True:
                    try:
                        given_input = int(input('Your value: '))
                    except:
                        print('You have to 1 or 11')
                        continue
                    if given_input == 1 or given_input == 11:
                        break
                    else:
                        continue
                player1.cards[p1_has_ace[x]].change_ace_value(given_input)

        #Player finished his turn, now its time to make computer cards visible
        player2.make_hidden(False)

        p2_cards_value = player2.calculate_cards_value()
        p1_cards_value = player1.calculate_cards_value()

        self.current_board(player1, player2)
        print(f'\nValue of cards in computer hand: {p2_cards_value}')
        print(f'Value of cards in player hand: {p1_cards_value}\n\n')
        
    def computer_turn(self, mydeck, player1, player2, player1_bet):
        '''
        This method dispalys current board state and ask player for his move
        INPUT: mydeck as Deck object, player1 and player2 as Player objects
        '''
        p2_cards_value = player2.calculate_cards_value()
        p1_cards_value = player1.calculate_cards_value()
        while True:
            p2_has_ace = player2.has_ace()
            if p1_cards_value>21:
                print('Player BUST, \nCOMPUTER WINS')
                break
            elif 21 >= p2_cards_value > p1_cards_value:
                print("Computer didn't pass 21 point\nComputer have higher score than player. \nCOMPUTER WINS!")
                break
            elif 21 == p1_cards_value == p2_cards_value:
                print("We have draw in this round")
                player1.balance += player1_bet
                break
            elif 21 >= p1_cards_value >= p2_cards_value:
                if p2_has_ace and 21 >= p2_cards_value+10 > p1_cards_value:
                    player2.cards[p2_has_ace[0]].value = 11
                    print(f'Computer changes value of Ace from 1 to 11\nNew computer hand value is: {p2_cards_value+10}')
                    print("Computer didn't pass 21 point\n Computer have higher score than player. \nCOMPUTER WINS!")
                    break
                else:
                    print("Computer didn't pass 21 point\n Computer have same or lower score than player.\nComputer will hit now")
                    input('Press ENTER to continue')
                    player2.hit(mydeck)
                    p2_cards_value = player2.calculate_cards_value()
                    self.current_board(player1, player2)
                    print(f'Value of cards in computer hand: {p2_cards_value}')
                    print(f'Value of cards in player hand: {p1_cards_value}')
                    continue
            else:
                print('Computer BUST,\n PLAYER WINS!!')
                player1.balance += player1_bet*2
                break
