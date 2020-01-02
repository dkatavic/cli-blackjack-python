"""
Players or dealer hand
"""

class Hand:
    def __init__(self, cards = None):
        """
        If I put cards = [] in parameter, reference points at the same object across invocations
        """
        if cards:
            self.cards = cards
        else:
            self.cards = []
    
    def append(self, card):
        self.cards.append(card)

    def __str__(self):
        deck = ""
        for card in self.cards:
            deck = deck + f"{card} "
        return deck
    
    def __len__(self):
        return len(self.cards)
    
    def __iter__(self):
        return iter(self.cards)
    

    