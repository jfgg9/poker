import random
suits = ["♠", "♥", "♦", "♣"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Deck(object):
    def __init__(self):
        self.cards = []
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        deck = ""
        for i in range(0, 52):
            deck += str(self.cards[i]) + " "
        return deck

    def take_one(self):
        return self.cards.pop(0)


class Hand(object):
    def __init__(self, deck):
        self.cards = []
        for i in range(5):
            self.cards.append(deck.take_one())

    def __str__(self):
        hand = ""
        for i in range(5):
            hand += str(self.cards[i]) + " "
        return hand

    def is_pair(self):
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    return True
        return False
   
    def is_twopair(self):
        pairs = 0
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    pairs += 1
        if pairs == 2:
            return True
        else:
            return False
    
    def is_four_of_a_kind(self):
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    for k in range(j+1, 5):
                        if self.cards[i].get_rank() == self.cards[k].get_rank():
                            for l in range(k+1, 5):
                                if self.cards[i].get_rank() == self.cards[l].get_rank():
                                    return True
        return False
    
    def is_three(self):
        for i in range(5):
            for j in range(i+1, 5):
                for k in range(j+1, 5):
                    if self.cards[i].get_rank() == self.cards[j].get_rank() and self.cards[j].get_rank() == self.cards[k].get_rank():
                        return True
        return False
    
    def is_flush(self):
        if self.cards[0].get_suit() == self.cards[1].get_suit() == self.cards[2].get_suit() == self.cards[3].get_suit() \
                == self.cards[4].get_suit():
            return True
        return False

for i in range(100000):
    new_deck = Deck()
    new_deck.shuffle()
    # print(new_deck)
    hand = Hand(new_deck)
    print(hand)
    if hand.is_pair():
        pair += 1
    elif hand.is_flush():
        flush += 1
    elif hand.is_three():
        three += 1
    elif hand.is_twopair():
        twopair += 1
    else:
        highcard += 1
        

print("Flush: ", flush)
print("Three of a Kind: ", three)
print("Two Pair: ", twopair)
print("Pair: ", pair)
print("High Card: ", highcard)

