from card import Card
from hand import PlayerHand, DealerHand
from shuffle import Shuffle

class Deck:
    """
    Card deck of 52 cards.

    >>> deck = Deck()
    >>> deck.get_cards()[:5]
    [(2, spades), (2, hearts), (2, diamonds), (2, clubs), (3, spades)]

    >>> deck.shuffle(modified_overhand=2, mongean=3)
    >>> deck.get_cards()[:5]
    [(A, spades), (Q, spades), (10, spades), (7, hearts), (5, hearts)]

    >>> hand = PlayerHand()
    >>> deck.deal_hand(hand)
    >>> deck.get_cards()[0]
    (Q, spades)
    """

    # Class Attribute(s)

    def __init__(self):
        """
        Creates a Deck instance containing cards sorted in ascending order.
        """
        suits = ['spades', 'hearts', 'diamonds', 'clubs']
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self, **shuffle_and_count):
        """Shuffles the deck using a variety of different shuffles.

        Parameters:
            shuffle_and_count: keyword arguments containing the
            shuffle type and the number of times the shuffled
            should be called.
        """
        assert all([isinstance(v, int) for v in shuffle_and_count.values()])
        assert all([isinstance(k, str) for k in shuffle_and_count.keys()])
        assert all([True if k in ["modified_overhand", "mongean"]\
        else False for k in shuffle_and_count.keys()])

        if "modified_overhand" not in shuffle_and_count.keys(): #means only mongean in shuffle
            for i in range(shuffle_and_count['mongean']):
                self.cards = Shuffle.mongean(self.cards)
        elif "mongean" not in shuffle_and_count.keys():
            self.cards = Shuffle.modified_overhand(self.cards, shuffle_and_count['modified_overhand'])
        else:
            self.cards = Shuffle.modified_overhand(self.cards, shuffle_and_count['modified_overhand'])
            for i in range(shuffle_and_count['mongean']):
                self.cards = Shuffle.mongean(self.cards)
        


    def deal_hand(self, hand):

        """
        Takes the first card from the deck and adds it to `hand`.
        """
        assert isinstance(hand, PlayerHand) or isinstance(hand, DealerHand)

        hand.add_card(self.cards[0])
        self.cards = self.cards[1:]
        
    def get_cards(self):
        return self.cards
