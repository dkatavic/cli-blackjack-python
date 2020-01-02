from playerBase import PlayerBase
from card import Card
from hand import Hand
import unittest

class PlayerBaseTest(unittest.TestCase):
    def test_get_single_card_score(self):
        hand = Hand([Card(2,'s')])
        base_player = PlayerBase(hand = hand)
        self.assertEqual(base_player.get_score(), 2)
    
    def test_get_score_with_king(self):
        hand = Hand([Card(2,'s'), Card(12, 's')])
        base_player = PlayerBase(hand = hand)
        self.assertEqual(base_player.get_score(), 12)
    
    def test_get_score_with_aces(self):
        tests = [
            {
                'cards': [Card(1,'s')],
                'expected': 11
            },
            {
                'cards': [Card(1,'s'), Card(13, 's')],
                'expected': 21
            },
            {
                'cards': [Card(1,'s'), Card(1,'s'), Card(13, 's')],
                'expected': 12
            }
        ]
        for test in tests:
            hand = Hand(test['cards'])
            base_player = PlayerBase(hand = hand)
            self.assertEqual(base_player.get_score(), test['expected'])

if __name__ == '__main__':
    unittest.main()