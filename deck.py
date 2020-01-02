from card import Card, SUITS
from random import randint

class Deck():
    def __init__(self):
        """
        Initialise deck with cards
        """
        cards = []
        for number in range(1,14):
            for suit in SUITS:
                cards.append(Card(number, suit))
        self.cards = cards
    
    def shuffle(self):
        # Copy so that shuffle is atomic
        old_cards = self.cards[:]
        new_cards = []
        while len(old_cards):
            random_card_index = randint(0, len(old_cards) - 1)
            new_cards.append(old_cards.pop(random_card_index))
        self.cards = new_cards
    
    def draw(self):
        if len(self.cards) <= 0:
            return None
        card = self.cards.pop()
        print(f'Drawing: {str(card)}')
        return card

    def __str__(self):
        deck = ""
        for card in self.cards:
            deck = deck + f"{card} "
        return deck
    
    def __len__(self):
        return len(self.cards)
    

            