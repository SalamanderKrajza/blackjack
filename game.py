'''
Milestone Project 2 - Blackjack Game

In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

    You need to create a simple text-based BlackJack game
    The game needs to have one player versus an automated dealer.
    The player can stand or hit.
    The player must be able to pick their betting amount.
    You need to keep track of the player's total money.
    You need to alert the player of wins, losses, or busts, etc...

And most importantly:

    You must use OOP and classes in some portion of your game.
    You can not just use functions in your game.
    Use classes to help you define the Deck and the Player's hand.
    There are many right ways to do this, so explore it well!

Feel free to expand this game. Try including multiple players.
Try adding in Double-Down and card splits!
Remember to you are free to use any resources you want and as always:
HAVE FUN!
'''

from blackjack.deck import Deck
from blackjack.card import Card #dont know if needed (deck.py is importhing card and comenting in isn't causing an error)
from blackjack.player import Player
from blackjack.thegame import TheGame

#====================================================
#▒█▀█▀█░▐█░▐█░▐█▀▀     ░▐█▀▀▀──░▄█▀▄─▒▐██▄▒▄██▌░▐█▀▀
#░░▒█░░░▐████░▐█▀▀     ░▐█░▀█▌░▐█▄▄▐█░▒█░▒█░▒█░░▐█▀▀
#░▒▄█▄░░▐█░▐█░▐█▄▄     ░▐██▄█▌░▐█─░▐█▒▐█░░░░▒█▌░▐█▄▄
#====================================================
game = TheGame()
player1 = Player('Player1') #player 1 is human
player2 = Player('Computer') #player 2 is a computer

#Before we start, we need to create deck
mydeck = Deck()
mydeck.shuffle()



#THis will be repeated until player decide to stop playing
while True:
    if player1.balance <=0:
        print('Player have not money anymore. Game is finished!')
        break
    #in case it is not first round we have to discard all cards from hand
    player1.discard_hand()
    player2.discard_hand()

    #Before game each player pick their cards, Human players have to make a bet
    player1_bet = player1.bet()

    #Then, each player have to pick 2 cards
    player1.pick_cards(mydeck)
    player2.pick_cards(mydeck)

    #Make one of computer cards hidden for player
    player2.make_hidden(True)

    #Player turn
    #Check if player BUST (21 points or more)
    #Until player pass 21 points there is still reason to ask him what he want to do
    game.player_turn(mydeck, player1, player2)

    #computer turn
    game.computer_turn(mydeck, player1, player2, player1_bet)
        
    #Ask player if he want to play another round
    given_input = ''
    while not given_input in ['yes', 'no']:
        given_input = input('\nDo you want to play another round [yes/no]?: ')

    if given_input == 'yes':
        print()
        pass
    else:
        print(f'Thank you for your time.\nYour final balance is {player1.balance}\n')
        break

