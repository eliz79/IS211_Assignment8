#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" A Timed Pig Dice Game - version 2."""

#Author: Erica Liz

import random
import sys
import argparse
import time

class Players():
    """ A constructor for Players."""
    def __init__(self):
        self.roll = True
        self.hold = False
        self.turn = False
        self.score = 0

    def choice(self):
        """A function for playing and/or passing."""
        decide = str(raw_input('Do you want to Roll (r) or Hold (h)? '))
        if decide == 'r':
            self.roll = True
            self.hold = False
        elif decide == 'h':
            self.roll = False
            self.hold = True
        else:
            print 'Invalid Entry. Do you want to Roll (r) or Hold (h)? '
            self.choice()

class ComputerPlayer(Players): #computer players
    """A strategy constructor for PC Players.""" #inherited from Players()
    def pc_choice(self):
        min_val = 25
        max_val = 100 - self.score
        if min_val < max_val:
            limit = min_val
        else:
            limit = max_val

        if self.score_turn < limit:
            print 'PC is rolling'
            self.hold = False
            self.roll = True
        else:
            print 'PC is holding'
            self.hold = True
            self.roll = False

class PlayerFactory(): #determines what type of player
    """A constructor for the correct player type."""

    def __init__(self):
        return None

    def correctplayer(self, player_type):
        """To determine who is playing."""

        if player_type == 'HUMAN':
            return Players()
        elif player_type == 'COMPUTER':
            return ComputerPlayer()
        else:
            print 'ERROR: Unknown Player'

class Game():
    """A constructor for a two player game called Pig Game."""
    def __init__(self, player1, player2, dice):
        self.player1 = player1
        self.player2 = player2
        self.player1.score = 0
        self.player2.score = 0
        self.player1.name = 'PLAYER 1'
        self.player2.name = 'PLAYER 2'
        self.dice = dice
        self.score_turn = 0
        flip = random.randint(1, 2) #random flip
        if flip == 1:
            self.cur_player = player1 #determines if player 1 will go first
            print 'The coin flip determined PLAYER 1 will begin.'
        elif flip == 2:
            self.cur_player = player2 #determines if player 2 will go first
            print 'The coin flip determined PLAYER 2 will begin.'
        else:
            print 'There was an Error, please try again.'
        self.player_turn()

    def next_turn(self): #will continue until a score of 100 is reached
        """Players next turn at rolling & total scores."""
        self.score_turn = 0
        if self.player1.score >= 100:
            print 'Player 1 has WON! The score is: ', self.player1.score
            sys.exit()
            newGame()
        elif self.player2.score >= 100:
            print 'Player 2 has WON! The score is: ', self.player2.score
            sys.exit() #exits game
            newGame()
        else:
            if self.cur_player == self.player1:
                self.cur_player = self.player2 #switches player
            elif self.cur_player == self.player2:
                self.cur_player = self.player1 #switches player
            else:
                print 'Error!!'
        print self.cur_player.name, 'WILL NOW PLAY.' #switches player
        self.player_turn()

    def player_turn(self):
        """A players turn at rolling."""
        print 'The total score for Player 1: ', self.player1.score
        print 'The total score for Player 2: ', self.player2.score
        self.dice.roll()
        if self.dice.val == 1:
            print 'You rolled a ''1'', No points earned, & you lost your turn'
            self.turn_score = 0 #no points earned on a roll of 1
            self.next_turn() #will move unto other player
        else:
            self.score_turn = self.score_turn + self.dice.val #adds players score for turn
            print 'You rolled a number: ', self.dice.val #tells what was rolled
            print 'You score this turn is: ', self.score_turn
            self.cur_player.choice()
            if self.cur_player.hold == True and self.cur_player.roll == False:
                self.cur_player.score = self.cur_player.score + self.score_turn
                #adds total player score
                self.next_turn()
            elif self.cur_player.hold == False and self.cur_player.roll == True:
                self.player_turn()                

class TimedGameProxy(Game): #Proxy class
    """Docstring."""
    def __init__(self):
        self.start = time.time()
        Game.__init__(self, player1='PLAYER1', player2='PLAYER2')

    def time_check(self): 
        """Docstring"""
        start = raw_input('Do you want to play a new timed game? Y/N ')
        if start == 'Y' or 'y':
            player1 = Players()
            player2 = Players()
            dice = Dice()
            new = Game(player1, player2, dice)
        elif start == 'N' or 'n':
            print 'Have a nice day!'

        if time.time() - self.start >= 60:
            print 'GAME OVER - Thank you for playing'
        elif self.player1.score > self.player2.score:
            print 'Player 1 has WON! Total score is: ', self.player1.score
        else:
            if self.player2.score > self.player1.score:
                print 'Player 2 has WON! Total score is: ', self.player2.score           
            sys.exit()
        
   
    def next_turn(self):
        """Players next turn at rolling & total scores."""
        self.score_turn = 0
        if self.player1.score >= 100:
            print 'Player 1 has WON! The score is: ', self.player1.score
            sys.exit()
            newGame()
        elif self.player2.score >= 100:
            print 'Player 2 has WON! The score is: ', self.player2.score
            sys.exit()
            newGame()
        else:
            if self.cur_player == self.player1:
                self.cur_player = self.player2
            elif self.cur_player == self.player2:
                self.cur_player = self.player1
            else:
                print 'Error!!'
        print self.cur_player.name, 'WILL NOW PLAY.' 
        self.player_turn()

    def player_turn(self):
        """A players turn at rolling."""
        print 'The total score for Player 1: ', self.player1.score
        print 'The total score for Player 2: ', self.player2.score
        self.dice.roll()
        if self.dice.val == 1:
            print 'You rolled a ''1'', No points earned, & you lost your turn'
            self.turn_score = 0
            self.next_turn()
        else:
            self.score_turn = self.score_turn + self.dice.val
            print 'You rolled a number: ', self.dice.val
            print 'You score this turn is: ', self.score_turn
            self.cur_player.choice()
            if self.cur_player.hold == True and self.cur_player.roll == False:
                self.cur_player.score = self.cur_player.score + self.score_turn
                self.next_turn()
            elif self.cur_player.hold == False and self.cur_player.roll == True:
                self.player_turn()

    def times_up():
        """Docstirng."""
        if self.player1.score > self.player2.score:
            print 'Time is up, PLAYER 1 has one!'
            sys.exit()

        elif self.player2.score > self.player1.score:
            print 'Time is up, PLAYER 2 has won!'
            sys.exit()

        else:
            print 'This is a TIE, noone wins!'
            sys.exit()

class Dice():
    """ A constructor for Dice."""
    def __init__(self):
        self.val = int()
        seed = 0 #sets a random seed for consistency

    def roll(self):
        """A random roll between 1-6."""
        self.val = random.randint(1, 6)

def newGame(): #combined instructions & new game
    """A function for playing or exiting the game."""
    print '\nWelcome to the Pig Dice Game'
    print '-----------------------------''\n'
    print 'How to Play: 2 Players Only'
    print ' ''\n'
    print 'Each turn, a player can roll the dice  to accumulate points. '
    print 'Any number rolled between 2-6 counts towards the total score. '
    print 'If a "1" is rolled points and turn is lost. Each player can choose. '
    print 'to roll or hold at any time unless a "1" is rolled; which at that'
    print 'moment you lose your turn and points.'
    print 'The player who totals 100 points WINS!'
    print ' ''\n'
    
    start = raw_input('Do you want to play? Y/N ')
    if start == 'Y'.lower():
        player1 = Players()
        player2 = Players()
        dice = Dice()
        new = Game(player1, player2, dice)
    elif start == 'N'.lower():
        print 'Have a nice day!'
        sys.exit()
    else:
        print 'Invalid entry, please try again. Enter ''y'' or ''n'''
        newGame()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--player1', help='State whether human or computer')
    parser.add_argument('--player2', help='Stat whether human or computer')
    parser.add_argument('--timed', help='Game is timed for 1 minute')
    args = parser.parse_args()

    if args.timed:
        time_game = TimedGameProxy()
    else:
        no_time_game = newGame()


if __name__ == '__main__':
    main()
