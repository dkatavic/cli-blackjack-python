from card import Card
import unittest

class CardTest(unittest.TestCase):
    def test_init_card(self):
        card = Card(1, 'c')
        self.assertEqual(card.__str__(), '1c')
    
    def test_card_suit_not_valid(self):
        self.assertRaises(BaseException, Card, 1, 'x')

    def test_number_suit_not_valid(self):
        self.assertRaises(BaseException, Card, 100, 'c')

if __name__ == '__main__':
    unittest.main()