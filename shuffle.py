class Shuffle:
    """
    Different kinds of shuffling techniques.
    
    >>> cards = [i for i in range(52)]
    >>> cards[25]
    25
    >>> mod_oh = Shuffle.modified_overhand(cards, 1)
    >>> mod_oh[0]
    25
    >>> mod_oh[25] 
    24
 
    >>> mongean_shuffle = Shuffle.mongean(mod_oh)
    >>> mongean_shuffle[0]
    51
    >>> mongean_shuffle[26]
    25

    >>> odd_cards = [1, 2, 3, 4, 5]
    >>> mongean_shuffle = Shuffle.mongean(odd_cards)
    >>> mongean_shuffle
    [4, 2, 1, 3, 5]

    
    >>> odd_cards = [1, 2, 3, 4, 5]
    >>> mod_oh_even = Shuffle.modified_overhand(odd_cards, 2)
    >>> mod_oh_even
    [1, 2, 3, 4, 5]

    >>> even_cards = [1,2,3,4,5,6]
    >>> mod_oh_odd = Shuffle.modified_overhand(even_cards, 3)
    >>> mod_oh_odd
    [2, 4, 1, 3, 5, 6]

    """     
        
    def modified_overhand(cards, num):
        """
        Takes `num` cards from the middle of the deck and puts them at the
        top. 
        Then decrement `num` by 1 and continue the process till `num` = 0. 
        When num is odd, the "extra" card is taken from the bottom of the
        top half of the deck.
        """
        
        # Use Recursion.
        # Note that the top of the deck is the card at index 0.
        assert num <= len(cards)
        assert isinstance(num, int) and isinstance(cards, list)
        if num == 0:
            return cards
        elif len(cards) % 2 == 1 and num % 2 == 1:
            temp_card = cards
            shuffle_card = temp_card[len(cards) // 2 - num//2: len(cards)//2 +\
                num//2 + 1]
            other_cards = temp_card[:len(cards) // 2 - num//2] +\
                temp_card[len(cards)//2 + num//2 + 1:]
            return Shuffle.modified_overhand(shuffle_card + other_cards, num - 1)
        elif len(cards) % 2 == 0 and num % 2 == 0:
            temp_card = cards
            shuffle_card = temp_card[len(cards) // 2 - num//2: len(cards)//2 +\
                num//2]
            other_cards = temp_card[:len(cards) // 2 - num//2] +\
                temp_card[len(cards)//2 + num//2:]
            return Shuffle.modified_overhand(shuffle_card + other_cards, num - 1)
        elif len(cards) % 2 == 1 and num % 2 == 0:
            temp_card = cards
            shuffle_card = temp_card[len(cards) // 2 - (num-1)//2: len(cards)//2 +\
                (num-1)//2 + 1]
            extra_card = [temp_card[(len(cards) // 2 - (num-1)//2)-1]]
            other_cards = temp_card[:(len(cards) // 2 - (num-1)//2)-1] +\
                temp_card[len(cards)//2 + (num-1)//2 + 1:]
            return Shuffle.modified_overhand(extra_card + shuffle_card +\
                other_cards, num - 1)
        elif len(cards) % 2 == 0 and num % 2 == 1:
            temp_card = cards
            shuffle_card = temp_card[len(cards) // 2 - num//2 - 1:\
                len(cards)//2 + num//2]
            other_cards = temp_card[:len(cards) // 2 - num//2 - 1] +\
                temp_card[len(cards)//2 + num//2:]
            return Shuffle.modified_overhand(shuffle_card + other_cards,\
            num - 1)
        
        
                    
    
    def mongean(cards):
        """
        Implements the mongean shuffle. 
        Check wikipedia for technique description. Doing it 12 times restores the deck.
        """
        
        # Remember that the "top" of the deck is the first item in the list.
        # Use Recursion. Can use helper functions.
        length_cards = len(cards)
        mong_shuffled = []
        def mong_shuffle(m_card):
            if len(m_card) == 0:
                return mong_shuffled
            elif (length_cards - len(m_card) + 1) % 2 == 0:
                mong_shuffled.insert(0, m_card[0])
                return mong_shuffle(m_card[1:])
            elif (length_cards - len(m_card) + 1) % 2 == 1:
                mong_shuffled.append(m_card[0])
                return mong_shuffle(m_card[1:])
        return mong_shuffle(cards)
