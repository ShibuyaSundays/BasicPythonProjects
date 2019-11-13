#starter code gathered from UT Austin Mitra CS 313 Problem Website
import random
class Card(object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    SUITS = ('C', 'D', 'H', 'S')
    def __init__(self, rank = 12, suit = 'S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12          
        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'
  # string representation of a Card object
    def __str__ (self):
        if (self.rank == 14):
            rank = 'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str (self.rank)
        return rank + self.suit
    # equality tests
    def __eq__ (self, other):
        return self.rank == other.rank
    def __ne__ (self, other):
        return self.rank != other.rank
    def __lt__ (self, other):
        return self.rank < other.rank
    def __le__ (self, other):
        return self.rank <= other.rank
    def __gt__ (self, other):
        return self.rank > other.rank
    def __ge__ (self, other):
        return self.rank >= other.rank

class Deck (object): # constructor
    def __init__ (self, num_decks = 1):
        self.deck = []
        for i in range (num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card (rank, suit)
                    self.deck.append (card)
    # shuffle the deck
    def shuffle (self):
        random.shuffle (self.deck)
    # deal a card
    def deal (self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)

class Poker (object): # constructor
    def __init__ (self, num_players = 2, num_cards = 5):
        self.deck = Deck()
        self.deck.shuffle()
        self.all_hands = []
        self.numCards_in_Hand = num_cards

    # deal the cards to the players
        for i in range (num_players):
            hand = []
            for j in range (self.numCards_in_Hand):
                hand.append (self.deck.deal())
            self.all_hands.append (hand)
    # simulate the play of poker
    """def is_royal (self, hand):
        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0, ''

        rank_order = true
        for i in range (len(hand)):
            rank_order = rank_order and (hand[i].rank == 14 - i)
        if (not rank_order):
            return 0, ''

        points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Royal Flush'

    def is_straight_flush (self, hand):
        same_suit = True
        for i in range(len(hand - 1)):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
        if (not same_suit):
            return 0, ''
        rank_order = True
        for i in range(len(hand - 1)):
            rank_order = rank_order and (hand[i].rank - 1 == hand[i + 1].rank)
        if(not rank_order):
            return 0, ''
        points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3\
                + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)

        return points, 'Straight Flush'

    def is_four_kind (self, hand):
        noFirst = 1
        noSecond = 1
        noCards = 0
        firstRank = hand[0].rank
        secondRank = 0
        for i in range(len(hand - 1)):
            if (hand[i].rank == hand[i + 1].rank):
                noFirst += 1
            else:
               noCards = i + 1
               secondRank = hand[i + 1].rank
               break
        for i in range(noCards, len(hand - 1)):
            if (hand[i].rank == hand[i + 1].rank):
                noSecond += 1
        if not(noFirst == 4 or noSecond == 4):
            return 0, ''
        if noFirst > noSecond:
            points = 8 * 15 ** 5 + (firstRank) * 15 ** 4 + (firstRank) * 15 ** 3\
                + (firstRank) * 15 ** 2 + (firstRank) * 15 ** 1 + (secondRank)
        else:
            points = 8 * 15 ** 5 + (secondRank) * 15 ** 4 + (secondRank) * 15 ** 3\
                + (secondRank) * 15 ** 2 + (secondRank) * 15 ** 1 + (firstRank)
        return points, 'Four of a Kind'
    def is_full_house (self, hand):
        noFirst = 1
        noSecond = 1
        noCards = 0
        firstRank = hand[0].rank
        secondRank = 0
        for i in range(len(hand - 1)):
            if (hand[i].rank == hand[i + 1].rank):
                noFirst += 1
            else:
                noCards = i + 1
                secondRank = hand[i + 1].rank
                break
        for i in range(noCards, len(hand - 1)):    
            if (hand[i].rank ==  hand[i + 1].rank):
                noSecond += 1
        if not((noFirst == 2 and noSecond == 3) or (noFirst == 3 and noSecond == 2)):
            return 0, ''
        if noFirst > noSecond:
            points = 7 * 15 ** 5 + (firstRank) * 15 ** 4 + (firstRank) * 15 ** 3\
                + (firstRank) * 15 ** 2 + (secondRank) * 15 ** 1 + (secondRank)
        else:
            points = 7 * 15 ** 5 + (secondRank) * 15 ** 4 + (secondRank) * 15 ** 3\
                + (secondRank) * 15 ** 2 + (firstRank) * 15 ** 1 + (firstRank)
        return points, 'Full House'

    def is_flush (self, hand):
        same_suit = True
        for i in range(len(hand - 1)):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
        if not(same_suit):
            return 0, ''
        points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3\
                + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)
        return points, 'Flush'

    def is_straight (self, hand):
        rank_order = True
        for i in range(len(hand - 1)):
            rank_order = rank_order and (hand[i].rank - 1 == hand[i + 1].rank)
        if not(rank_order):
            return 0, ''
        points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3\
                + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)
        return points, 'Straight'

    def is_three_kind (self, hand):
        count = 1
        cardRank = hand[1].rank
        exCard1 = 0
        exCard2 = 0
        for i in range(len(hand - 1)):
            if(hand[i].rank == hand[i + 1].rank):
                count += 1
            else:
                count = 1
                cardRank = hand[i + 1].rank
        if not(count == 3):
            return 0, ''
        for i in range(len(hand)):
            if(hand[i].rank != cardRank and exCard1 > 0):
                exCard2 == hand[i].rank
            if(hand[i].rank != cardRank and exCard1 == 0):
                exCard1 = hand[i].rank
        if(exCard2 > exCard1):
            temp = exCard1
            exCard1 = exCard2
            exCard2 = temp
            
        points = 4 * 15 ** 5 + (cardRank) * 15 ** 4 + (cardRank) * 15 ** 3\
                + (cardRank) * 15 ** 2 + (exCard1) * 15 ** 1 + (exCard2)
        return points, 'Three of a Kind'
    def is_two_pair (self, hand):
        pair1 = False
        pair2 = False
        pair1Rank = 0
        pair2Rank = 0
        randRank = 0
        for i in range(len(hand - 1)):
            if(hand[i].rank == hand[i + 1].rank and pair1 == True):
                pair2 = True
                pair2Rank = hand[i].rank
            if(hand[i].rank == hand[i + 1].rank and pair1 == False):
                pair1 = True
                pair1Rank = hand[i].rank
        if not(pair1 and pair2):
            return 0, ''
        if(pair2Rank > pair1Rank):
            temp = pair1Rank
            pair1Rank = pair2Rank
            pair2Rank = temp
        for i in range(len(hand)):
            if(hand[i].rank != pair1Rank and hand[i].rank != pair2Rank):
                randRank = hand[i].rank
        points = 3 * 15 ** 5 + (pair1Rank) * 15 ** 4 + (pair1Rank) * 15 ** 3\
                + (pair2Rank) * 15 ** 2 + (pair2Rank) * 15 ** 1 + randRank
        return points, 'Two Pair'
  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
    def is_one_pair (self, hand):
        one_pair = False
        pairRank = 0
        randRank = [0, 0, 0]
        for i in range (len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                pairRank = hand[i].rank 
                one_pair = True
                break
        if (not one_pair):
            return 0, ''
        for i in range(len(hand)):
            if(hand[i].rank != pairRank and randRank[2] > 0 and randRank[1] > 0):
                randRank[0] = hand[i].rank
            if(hand[i].rank != pairRank and randRank[2] > 0 and randRank[1] == 0):
                randRank[1] = hand[i].rank
            if(hand[i].rank != pairRank and randRank[2] == 0):
                randRank[2] = hand[i].rank
        randRank.sort() 
        points = 2 * 15 ** 5 + (pairRank) * 15 ** 4 + (pairRank) * 15 ** 3
        points = points + (randRank[2]) * 15 ** 2 + (randRank[1]) * 15 ** 1
        points = points + (randRank[0])
        return points, 'One Pair'

    def is_high_card (self,hand):
        points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3\
                + hand[2].rank * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)
        return points, 'High Card'"""
   # determine the type of each hand and print

    def play (self):
    # sort the hands of each player print
        def is_royal (self, hand):
            same_suit = True
            for i in range (len(hand) - 1):
                same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
    
            if (not same_suit):
                return 0, ''
    
            rank_order = True
            for i in range (len(hand)):
                rank_order = rank_order and (hand[i].rank == 14 - i)
            if (not rank_order):
                return 0, ''
    
            points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
            points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
            points = points + (hand[4].rank)
    
            return points, 'Royal Flush'
    
        def is_straight_flush (self, hand):
            same_suit = True
            for i in range(len(hand) - 1):
                same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
            if (not same_suit):
                return 0, ''
            rank_order = True
            for i in range(len(hand) - 1):
                rank_order = rank_order and (hand[i].rank - 1 == hand[i + 1].rank)
            if(not rank_order):
                return 0, ''
            points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3\
                    + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)
    
            return points, 'Straight Flush'
    
        def is_four_kind (self, hand):
            noFirst = 1
            noSecond = 1
            noCards = 0
            firstRank = hand[0].rank
            secondRank = 0
            for i in range(len(hand) - 1):
                if (hand[i].rank == hand[i + 1].rank):
                    noFirst += 1
                else:
                   noCards = i + 1
                   secondRank = hand[i + 1].rank
                   break
            for i in range(noCards, len(hand) - 1):
                if (hand[i].rank == hand[i + 1].rank):
                    noSecond += 1
            if not(noFirst == 4 or noSecond == 4):
                return 0, ''
            if noFirst > noSecond:
                points = 8 * 15 ** 5 + (firstRank) * 15 ** 4 + (firstRank) * 15 ** 3\
                    + (firstRank) * 15 ** 2 + (firstRank) * 15 ** 1 + (secondRank)
            else:
                points = 8 * 15 ** 5 + (secondRank) * 15 ** 4 + (secondRank) * 15 ** 3\
                    + (secondRank) * 15 ** 2 + (secondRank) * 15 ** 1 + (firstRank)
            return points, 'Four of a Kind'
        def is_full_house (self, hand):
            noFirst = 1
            noSecond = 1
            noCards = 0
            firstRank = hand[0].rank
            secondRank = 0
            for i in range(len(hand) - 1):
                if (hand[i].rank == hand[i + 1].rank):
                    noFirst += 1
                else:
                    noCards = i + 1
                    secondRank = hand[i + 1].rank
                    break
            for i in range(noCards, len(hand) - 1):    
                if (hand[i].rank ==  hand[i + 1].rank):
                    noSecond += 1
            if not((noFirst == 2 and noSecond == 3) or (noFirst == 3 and noSecond == 2)):
                return 0, ''
            if noFirst > noSecond:
                points = 7 * 15 ** 5 + (firstRank) * 15 ** 4 + (firstRank) * 15 ** 3\
                    + (firstRank) * 15 ** 2 + (secondRank) * 15 ** 1 + (secondRank)
            else:
                points = 7 * 15 ** 5 + (secondRank) * 15 ** 4 + (secondRank) * 15 ** 3\
                    + (secondRank) * 15 ** 2 + (firstRank) * 15 ** 1 + (firstRank)
            return points, 'Full House'
    
        def is_flush (self, hand):
            same_suit = True
            for i in range(len(hand) - 1):
                same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
            if not(same_suit):
                return 0, ''
            points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3\
                    + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)
            return points, 'Flush'
    
        def is_straight (self, hand):
            rank_order = True
            for i in range(len(hand) - 1):
                rank_order = rank_order and (hand[i].rank - 1 == hand[i + 1].rank)
            if not(rank_order):
                return 0, ''
            points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3\
                    + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)
            return points, 'Straight'
    
        def is_three_kind (self, hand):
            count = 1
            cardRank = hand[1].rank
            exCard1 = 0
            exCard2 = 0
            for i in range(len(hand) - 1):
                if(hand[i].rank == hand[i + 1].rank):
                    count += 1
                else:
                    count = 1
                    cardRank = hand[i + 1].rank
            if not(count == 3):
                return 0, ''
            for i in range(len(hand)):
                if(hand[i].rank != cardRank and exCard1 > 0):
                    exCard2 == hand[i].rank
                if(hand[i].rank != cardRank and exCard1 == 0):
                    exCard1 = hand[i].rank
            if(exCard2 > exCard1):
                temp = exCard1
                exCard1 = exCard2
                exCard2 = temp
                
            points = 4 * 15 ** 5 + (cardRank) * 15 ** 4 + (cardRank) * 15 ** 3\
                    + (cardRank) * 15 ** 2 + (exCard1) * 15 ** 1 + (exCard2)
            return points, 'Three of a Kind'
        def is_two_pair (self, hand):
            pair1 = False
            pair2 = False
            pair1Rank = 0
            pair2Rank = 0
            randRank = 0
            for i in range(len(hand) - 1):
                if(hand[i].rank == hand[i + 1].rank and pair1 == True):
                    pair2 = True
                    pair2Rank = hand[i].rank
                if(hand[i].rank == hand[i + 1].rank and pair1 == False):
                    pair1 = True
                    pair1Rank = hand[i].rank
            if not(pair1 and pair2):
                return 0, ''
            if(pair2Rank > pair1Rank):
                temp = pair1Rank
                pair1Rank = pair2Rank
                pair2Rank = temp
            for i in range(len(hand)):
                if(hand[i].rank != pair1Rank and hand[i].rank != pair2Rank):
                    randRank = hand[i].rank
            points = 3 * 15 ** 5 + (pair1Rank) * 15 ** 4 + (pair1Rank) * 15 ** 3\
                    + (pair2Rank) * 15 ** 2 + (pair2Rank) * 15 ** 1 + randRank
            return points, 'Two Pair'
  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
        def is_one_pair (self, hand):
            one_pair = False
            pairRank = 0
            randRank = [0, 0, 0]
            for i in range (len(hand) - 1):
                if (hand[i].rank == hand[i + 1].rank):
                    pairRank = hand[i].rank 
                    one_pair = True
                    break
            if (not one_pair):
                return 0, ''
            for i in range(len(hand)):
                if(hand[i].rank != pairRank and randRank[2] > 0 and randRank[1] > 0):
                    randRank[0] = hand[i].rank
                if(hand[i].rank != pairRank and randRank[2] > 0 and randRank[1] == 0):
                    randRank[1] = hand[i].rank
                if(hand[i].rank != pairRank and randRank[2] == 0):
                    randRank[2] = hand[i].rank
            randRank.sort() 
            points = 2 * 15 ** 5 + (pairRank) * 15 ** 4 + (pairRank) * 15 ** 3
            points = points + (randRank[2]) * 15 ** 2 + (randRank[1]) * 15 ** 1
            points = points + (randRank[0])
            return points, 'One Pair'
    
        def is_high_card (self,hand):
            points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3\
                    + hand[2].rank * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)
            return points, 'High Card'
       # determine the type of each hand and print
        
        for i in range (len(self.all_hands)):
            sorted_hand = sorted (self.all_hands[i], reverse = True)
            self.all_hands[i] = sorted_hand
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str (card) + ' '
            print ('Player ' + str(i + 1) + ' : ' + hand_str)

        hand_type = []	# create a list to store type of hand
        hand_points = []	# create a list to store points for hand
        hand_type_str = []
        for i in range(len(self.all_hands)):  #iterate for all players again
            pts = 0
            pts, typ = is_royal(self, self.all_hands[i])
            if pts > 0: 
                hand_points.append((pts, i))
                hand_type.append((10, i))
                hand_type_str.append(typ)
                continue
            pts, typ = is_straight_flush(self, self.all_hands[i]) 
            if pts > 0: 
                hand_points.append((pts, i))
                hand_type.append((9, i))
                hand_type_str.append(typ)
                continue
            pts, typ = is_four_kind(self, self.all_hands[i]) 
            if pts > 0: 
                hand_points.append((pts, i))
                hand_type.append((8, i))
                hand_type_str.append(typ)
                continue
            pts, typ = is_full_house(self, self.all_hands[i]) 
            if pts > 0: 
                hand_points.append((pts, i))
                hand_type.append((7, i))
                hand_type_str.append(typ)
                continue
            pts, typ = is_flush(self, self.all_hands[i]) 
            if pts > 0: 
                hand_points.append((pts, i))
                hand_type.append((6, i))
                hand_type_str.append(typ)
                continue
            pts, typ = is_straight(self, self.all_hands[i]) 
            if pts > 0: 
                hand_points.append((pts, i))
                hand_type.append((5, i))
                hand_type_str.append(typ)
                continue
            pts, typ = is_three_kind(self, self.all_hands[i]) 
            if pts > 0: 
                hand_points.append((pts, i))
                hand_type.append((4, i))
                hand_type_str.append(typ)
                continue
            pts, typ = is_two_pair(self, self.all_hands[i]) 
            if pts > 0: 
                hand_points.append((pts, i))
                hand_type.append((3, i))
                hand_type_str.append(typ)
                continue
            pts, typ = is_one_pair(self, self.all_hands[i]) 
            if pts > 0: 
                hand_points.append((pts, i))
                hand_type.append((2, i))
                hand_type_str.append(typ)
                continue
            pts, typ = is_high_card(self, self.all_hands[i]) 
            if pts > 0: 
                hand_points.append((pts, i))
                hand_type.append((1, i))
                hand_type_str.append(typ)
                continue
        hand_type.sort(reverse = True)
        #hand_points.sort(reverse = True)
        tie_list = []
        i = 0
        for i in range(len(hand_type)):
            if hand_type[i][0] == hand_type[0][0]:
                index = int(hand_type[i][1])
                tie_list.append((hand_points[index], index))
        tie_list.sort(reverse = True)
        print('\n')
        for i in range(len(self.all_hands)):
            print ('Player ' + str(i + 1) + ' : ' + str(hand_type_str[i]))
        print('\n') 
        if len(tie_list) == 1:
            print ('Player ' + str(tie_list[0][1] + 1) + ' wins.')
        else:
            for i in range(len(tie_list)):
                print ('Player ' + str(tie_list[i][1] + 1) + ' ties.')
def main():
    num_players = int(input ('Enter number of players: '))
    while ((num_players < 2) or (num_players > 6)):
        num_players = int (input ('Enter number of players: '))
  # create the Poker object
    game = Poker (num_players)
  # play the game
    game.play()

main()
