class Card:
    """
    Card class.

    # Doctests for str and repr
    >>> card_1 = Card("A", "spades")
    >>> print(card_1)
    ____
    |A  |
    | ♠ |
    |__A|
    >>> card_1
    (A, spades)
    >>> card_2 = Card("K", "spades")
    >>> print(card_2)
    ____
    |K  |
    | ♠ |
    |__K|
    >>> card_2
    (K, spades)
    >>> card_3 = Card("A", "diamonds")
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)

    # Doctests for comparisons
    >>> card_1 < card_2
    False
    >>> card_1 > card_2
    True
    >>> card_3 > card_1
    True

    # Doctests for set_visible()
    >>> card_3.set_visible(False)
    >>> print(card_3)
    ____
    |?  |
    | ? |
    |__?|
    >>> card_3
    (?, ?)
    >>> card_3.set_visible(True)
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)
    """

    # Class Attribute(s)

    def __init__(self, rank, suit, visible=True):
        """
        Creates a card instance and asserts that the rank and suit are valid.
        """
        assert isinstance(rank,int) or isinstance(rank,str)
        if isinstance(rank, int):
            assert rank >= 2 and rank <= 10
        assert isinstance(suit, str)
        assert suit in ["hearts", "diamonds", "clubs", "spades"]
        assert isinstance(visible, bool)
        self.rank = rank #int or str
        self.suit = suit
        self.visible = visible
        

    def __lt__(self, other_card):
        rank_ranking = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        suit_ranking = ['spades', 'hearts', 'diamonds', 'clubs']
        if self.get_rank() != other_card.get_rank():
            if rank_ranking.index(self.get_rank()) < rank_ranking\
            .index(other_card.get_rank()):
                return True
            else:
                return False
        elif self.get_rank() == other_card.get_rank():
            if suit_ranking.index(self.get_suit()) < suit_ranking\
            .index(other_card.get_suit()):
                return True
            else:
                return False
            


    def __str__(self):
        """
        Returns ASCII art of a card with the rank and suit. If the card is
        hidden, question marks are put in place of the actual rank and suit.

        Examples:
        ____
        |A  |
        | ♠ |
        |__A|
        ____
        |?  |
        | ? |
        |__?|             
        """
        rank = str(self.get_rank())
        if self.visible == False:
            return '____' + '\n' + \
               '|{}  |'.format("?") + '\n' + \
               '| {} |'.format("?") + '\n' + \
               '|__{}|'.format("?")
        else:
            if self.get_suit() == 'hearts':
                suit = '♥'
            elif self.get_suit() == 'spades':
                suit = '♠'
            elif self.get_suit() == 'clubs':
                suit = '♣'
            elif self.get_suit() == 'diamonds':
                suit = '♦'
            return '____' + '\n' + \
                '|{x}  |'.format(x = rank) + '\n' + \
                '| {y} |'.format(y = suit) + '\n' + \
                '|__{x}|'.format(x = rank)

    def __repr__(self):
        """
        Returns (<rank>, <suit>). If the card is hidden, question marks are
        put in place of the actual rank and suit.           
        """
        if self.visible == True:
            return "({}, {})".format(self.get_rank(), self.get_suit())
        else:
            return "({}, {})".format("?", "?")

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit

    def set_visible(self, visible):
        assert isinstance(visible, bool)
        self.visible = visible
        return

    