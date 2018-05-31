# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ''
score = 0
busted = ''

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []	# create Hand object

    def __str__(self):
        obj = 'Hand contains '	# return a string representation of a hand
        for i in self.cards:
            obj += str(i) + ' '
        return obj

    def add_card(self, card):
        self.cards.append(card)	# add a card object to a hand

    def get_value(self):
        v = 0
        r = []
        for i in self.cards: # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
            v += VALUES[i.get_rank()]
            r.append(i.get_rank())
        if 'A' in r:
            return v + 10 if v + 10 <= 21 else v	# compute the value of the hand, see Blackjack video
        else:
            return v
          
   
    def draw(self, canvas, pos):
        for i in range(len(self.cards)):# draw a hand on the canvas, use the draw method for cards
            self.cards[i].draw(canvas,[pos[0]+72*i,pos[1]])
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []	# create a Deck object
        for s in SUITS:
            for r in RANKS:
                self.cards.append(Card(s,r))

    def shuffle(self):
        random.shuffle(self.cards)# shuffle the deck 
        
    def deal_card(self):
        d = self.cards[-1]	# deal a card object from the deck
        self.cards.remove(d)
        return d
    
    def __str__(self):
        obj = 'Deck contains '	# return a string representing the deck
        for i in self.cards:
            obj += str(i) + ' '
        return obj



#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, deck, score, busted
    if in_play == True:
        score -= 1
    outcome = 'Hit or Stand?'
    busted = ''
    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    in_play = True

def hit():
    global in_play, outcome, score, busted
    if player.get_value() <= 21 and in_play == True:
        player.add_card(deck.deal_card())
        if player.get_value() > 21:
            outcome = 'You lose. New Deal?!'
            busted = 'You have busted.'
            in_play = False
            score -= 1
            
def stand():
    global in_play, outcome, score, busted
    if not in_play:
        return 0
    else:
        in_play = False
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    while dealer.get_value() < 17:
        dealer.add_card(deck.deal_card())
    # assign a message to outcome, update in_play and score
    if dealer.get_value() < player.get_value():
        outcome = 'You win. New Deal?'
        busted = 'Your value is higher.'
        score += 1
    elif dealer.get_value() > 21:
        busted = 'Dealer has busted.'
        outcome = 'You win. New Deal?'
        score += 1
    else:
        outcome = 'You lose. New Deal?'
        busted = "Dealer's value is higher or tie."
        score -= 1
        
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('Blackjack', [100, 40], 30, 'Yellow')
    canvas.draw_text('Dealer', [100, 170], 25, 'Black')
    canvas.draw_text('Player', [100, 370], 25, 'Black')
    canvas.draw_text(outcome, [300, 370], 25, 'Yellow')
    canvas.draw_text(busted, [300, 170], 25, 'Yellow')
    canvas.draw_text('Score: '+str(score), [100, 80], 25, 'Yellow')
    dealer.draw(canvas, [100,200])
    player.draw(canvas, [100,400])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_SIZE, [100+CARD_BACK_CENTER[0], 200+CARD_BACK_CENTER[1]], CARD_SIZE)
        

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric