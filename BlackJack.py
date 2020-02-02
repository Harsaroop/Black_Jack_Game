# IMPORT STATEMENTS AND VARIABLE DECLARATIONS:

import random


suits = ('Hearts','Diamonds','Spades','Clubs') #An Array stroing the suits of the card
ranks = ('Two' , 'Three' , 'Four' , 'Five' , 'Six' , 'Seven' , 'Eight' , 'Nine' , 'Ten' , 'Jack' , 'Queen' , 'King' , 'Ace') #

values = {'Two':2 , 'Three':3 , 'Four':4 , 'Five':5 , 'Six':6 , 'Seven':7 , 'Eight':8 , 'Nine':9 , 'Ten':10 , 'Jack':10 ,
          'Queen':10 , 'King':10 , 'Ace':11}

playing = True

#Class Definitions

class Card():
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        
    def __str__(self):
        return self.rank+" of "+self.suit

class Deck():
    
    def __init__(self):
        self.deck = []
        for s in suits:
            for r in ranks:
                self.deck.append(Card(s,r))
                
    def __str__(self):
        deck_52 = ''
        for i in self.deck:
            deck_52 += '\n '+i.__str__()
        return deck_52
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand():
    
    def __init__(self,):
        self.card = []
        self.value = 0
        self.aces = 0
        
    def add_card(self,card):
        self.card.append(card)
        self.value += values[card.rank]
        
        if card.rank == 'Aces':
            self.aces += 1
        
    def adjust_for_aces(self):
        while self.aces > 21 and self.aces:
            self.values -= 10
            self.aces -= 1

class chips():
    
    def __init__(self,total=100):
        self.total = total
        self.bet = 0
        
    def winning_bet(self):
        self.total += self.bet
        
    def losing_bet(self):
        self.total -= self.bet

#IMPORTANT AND FREQUENTLY USED FUNCTIONS

def take_bet(chips):
    
    while True:
        
        try:
            chips.bet = int(input('How much do you want to input? '))
        except:
            ("Please enter an integer")
        else:
            if chips.bet > chips.total :
                ("Sorry not enough Money")
            else:
                break

def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_aces()
    
def hit_or_stand(deck,hand):
    global playing
    
    while True:
    
        turn = input("Would ypu like to hit or Stand (h or s)")
        
        if turn[0].lower() == 'h':
            hit(deck,hand)
            playing = True
            
        elif turn[0].lower() == 's':
            print('Player Stands. Dealer''s turn ')            
            playing = False
        else:
            print('Sorry Try again')
            continue
        break
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.card[1])  
    print("\nPlayer's Hand:", *player.card, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.card, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.card, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
        print('Player Bust')
        chips.losing_bet()
        
def player_wins(player,dealer,chips):
        print('Player Wins')
        chips.winning_bet()
        
def dealer_busts(player,dealer,chips):
        print('Player Wins! Dealer Busts')
        chips.winning_bet()
    
def dealer_wins(player,dealer,chips):
        print('Dealer Wins!')
        chips.losing_bet()
        
        
def push(player,dealer,chips):
    print('Dealer and Player tie! PUSH')

#GAMEPLAY

while True:
    # Print an opening statement
    print('welcome to the Blackjack Game')
    
    # Create & shuffle the deck, deal two cards to each player
    new_deck = Deck()
    new_deck.shuffle()
    
    player = Hand()
    player.add_card(new_deck.deal())
    player.add_card(new_deck.deal())
    
    dealer = Hand()
    dealer.add_card(new_deck.deal())
    dealer.add_card(new_deck.deal())
        
    # Set up the Player's chips
    player_chips = chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(new_deck,player)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_bust(player,dealer,chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value <= 21 :
        
        while dealer.value < 17:
            hit(new_deck,dealer)
    
        # Show all cards
        show_all(player,dealer)
        
        # Run different winning scenarios
        if dealer.value > 21:
            dealer_busts(player,dealer,player_chips)
            
        elif dealer.value > player.value:
            dealer_wins(player,dealer,player_chips)
            
        elif dealer.value < player.value:
            player_wins(player,dealer,player_chips)
            
        else:
            push(player,dealer,chips)
            
    # Inform Player of their chips total 
    print('Chips Left are {}'.format(player_chips.total))
    # Ask to play again
    new_game = input('Do you want to play again Yes or No')
    
    if new_game[0].lower() == 'y':
        playing = True
    else:
        print('GoodBye')
        break