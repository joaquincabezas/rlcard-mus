import os
import json
import numpy as np
from collections import OrderedDict

import rlcard

from rlcard.games.mus.card import MusCard as Card

def init_spanish_deck():
    ''' Initialize a Spanish deck of 40 cards

    Returns:
        (list): A list of Card object
    '''
    suit_list = ['O', 'C', 'E', 'B'] # Oros, Copas, Espadas, Bastos
    rank_list = ['1', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']
    res = [Card(suit, rank) for suit in suit_list for rank in rank_list]
    return res
