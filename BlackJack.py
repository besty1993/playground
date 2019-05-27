import random

def Score(hand) :
    score = 0
    aces = 0
    for card in hand :
        if card in [2,3,4,5,6,7,8,9] :
            score += card
        elif card in [10,11,12,13] :
            score += 10
        else :
            aces += 1
    if score+aces*11 > 21 :
        return score+aces
    else :
        return score+aces*11

class BlackJack () :
    def __init__ (self, n, strategy) :        
        self.deck = [2,3,4,5,6,7,8,9,10,11,12,13,1] *4
        random.shuffle(self.deck)
        
        self.playerHand = []
        self.dealerHand = []
        self.hit(self.playerHand)
        self.hit(self.playerHand)
        self.hit(self.dealerHand)
        self.hit(self.dealerHand)
        
        self.usedCards = []
        self.game_result = []
        
        for i in range(n) :
            print(self.deck)
            self.player_play(strategy)
            self.turn_end_and_dealer_play()
            self.finish(i)
            self.preparation()
            
    def preparation(self) :
        self.usedCards = self.usedCards + self.playerHand + self.dealerHand
        temp = self.usedCards
        self.playerHand = []
        self.dealerHand = []
        self.hit(self.playerHand)
        self.hit(self.playerHand)
        self.hit(self.dealerHand)
        self.hit(self.dealerHand)
        return
        
    def reshuffle(self) :
        if not len(self.deck) ==  0 : return
        else :
            self.deck = self.usedCards
            self.usedCards = []
            random.shuffle(self.deck)
#             print("Reshuffled")
            return
        
        

        
    def hit(self,hand) :
        if len(self.deck) == 0 :
            self.reshuffle()
        card = self.deck.pop()
#         print(str(hand) +" hit! "+ str(card))
        hand.append(card)
        return hand
    
    def turn_end_and_dealer_play(self) :
        while Score(self.dealerHand) < 17 :
            self.hit(self.dealerHand)
        return self
    
    def player_play(self, strategy) :
        while True :
            player = self.playerHand
            dealer = self.dealerHand
            used = self.usedCards
            if strategy(player, [dealer[0]], used) :
                self.hit(self.playerHand)
            else :
                break
        return self
    
    def finish(self, gameNum) :
        playerScore = Score(self.playerHand)
        dealerScore = Score(self.dealerHand)
#         print("GAME"+str(gameNum)+", Player : " + str(playerScore) + ", Dealer : " + str(dealerScore), end=', ')
        print("GAME {}: Player {}, Dealer {}".format(gameNum+1, playerScore, dealerScore), end=', ')
        if playerScore > 21:
            print("Dealer Win")
            self.game_result.append(False)
            return False
        elif playerScore == 21 or playerScore > dealerScore or dealerScore >21 :
            print("Player Win")
            self.game_result.append(True)
            return True
        elif playerScore == dealerScore :
            print("Draw")
            self.game_result.append(False)
        else :
            print("Dealer Win")
            self.game_result.append(False)
            return False

def strategy (player, dealer, used) :
    return Score(player) < 17

A = BlackJack(500, strategy)
print(sum(A.game_result)/len(A.game_result))
