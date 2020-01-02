from deck import Deck
from card import Card
import unittest

class DeckTest(unittest.TestCase):
    def test_init_deck(self):
        deck = Deck()
        number_of_cards = len(deck.cards)
        self.assertEqual(number_of_cards, 52)
    
    def test_shuffle_deck(self):
        deck = Deck()
        initial_deck = deck.__str__()
        deck.shuffle()
        final_deck = deck.__str__()
        self.assertNotEqual(initial_deck, final_deck)
    
    def test_draw_card(self):
        deck = Deck()
        expected = Card(13, 's')
        self.assertEqual(len(deck), 52)
        self.assertEqual(deck.draw(), expected)
        self.assertEqual(len(deck), 51)

if __name__ == "__main__":
    unittest.main()