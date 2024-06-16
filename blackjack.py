from random import shuffle

class Card():
    suits = [ "spades" , "hearts" , "diamonds" , "clubs" ]
    values = [None,None,"2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" ,"10" , "Jack" , "Queen" , "King" , "Ace" ]

    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.values[self.value]} of {self.suits[self.suit]}'

class Deck():
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(0,4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Hand():
    def __init__(self):
        self.cards = []
        # self.turn = True

    def get_value(self):
        self.value = 0
        num_ace = 0
        for i in self.cards:
            if i.value >=11 and i.value <=13:
                self.value+=10
            elif i.value == 14:
                self.value+=11
            else:
                self.value+=i.value
        
        while self.value > 21 and num_ace:
            self.value-=10
            num_ace-=1
        return self.value

class Blackjack():
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        for i in range(2):
            self.player_hand.cards.append(self.deck.deal_card())
            self.dealer_hand.cards.append(self.deck.deal_card())

    def players_turn(self):
        print(f'the dealer face up card is {self.dealer_hand.cards[0]}')
        print(f'your cards are {self.player_hand.cards[0]},{self.player_hand.cards[1]}')
        print(f'your value is {self.player_hand.get_value()}')
        while True:
            choice = input("what would you like to do (h/s):")
            if choice == "h":
                self.player_hand.cards.append(self.deck.deal_card())
                for i in self.player_hand.cards:
                    print(i)
                print(f'your value is {self.player_hand.get_value()}')
            else:
                break
    
    def dealer_turn(self):
        print(f"the dealer's second card is {self.dealer_hand.cards[1]}")
        while self.dealer_hand.get_value() < 17:
            self.dealer_hand.cards.append(self.deck.deal_card())
            print('dealer Hits')
        print(f"the dealers value is {self.dealer_hand.get_value()}")
    
    def winner(self):
        if self.dealer_hand.get_value() >21 :
            return "dealer's hand is a bust, you won"

        elif self.player_hand.get_value() >21:
            return "It's a bust, you lost"
        
        elif self.dealer_hand.get_value() == 21 and self.player_hand.get_value()!= 21:
            return "Blackjack You lost" 
        elif self.player_hand.get_value() == 21 and self.dealer_hand.get_value()!= 21:
            return 'Blackjack You won'
        
        if self.player_hand.get_value() == self.dealer_hand.get_value():
            return "It's a tie"
        
        if self.player_hand.get_value() > self.dealer_hand.get_value():
            return "You won"
        else:
            return "you lost"

    def gameplay(self):
        print("Welcome to blackjack!")
        self.players_turn()
        self.dealer_turn()
        print("\n"+self.winner())    

game = Blackjack()
game.gameplay()

