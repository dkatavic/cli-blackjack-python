"""
Suits:
 * d - diamonds (♦)
 * c - clubs (♣)
 * h - hearts (♥)
 * s - spades (♠)
"""
SUITS = ('d', 'c', 'h', 's')

class Card:
    def __init__(self, number, suit):
        if suit not in SUITS:
            raise BaseException(f'suit: "{suit} not in a {SUITS}')
        self.suit = suit
        if not 1 <= number <= 13:
            raise BaseException(f'number: "{number} not in a range between 1 and 13')
        self.number = number
    
    def __str__(self):
        return str(self.number) + self.suit
    
    def __eq__(self, other):
        return self.__str__() == other.__str__()
