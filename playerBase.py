from hand import Hand

class PlayerBase:

    def __init__(self, name = "John Doe", hand = Hand()):
        self.hand = hand
        self.name = name
    
    def get_score(self):
        score = 0
        # Filter aces first
        for card in filter(lambda c: c.number > 1, self.hand):
            # J, Q, K
            if card.number > 10:
                score += 10
            else:
                score += card.number
        # Calculate aces
        aces = list(filter(lambda c: c.number == 1, self.hand))
        num_aces = len(aces)
        # Scores under or equal 21
        valid_scores = []
        # Scores over 21
        busted_scores = []
        for i in range(0, num_aces + 1):
            cur_score = score + i * 11 + (num_aces - i) * 1
            if cur_score > 21:
                busted_scores.append(cur_score)
            else:
                valid_scores.append(cur_score)
        if (len(valid_scores) > 0):
            valid_scores.sort()
            return valid_scores[-1]
        else:
            busted_scores.sort()
            return busted_scores[0]

    def add_card(self, card):
        self.hand.append(card)
    
    def reset_hand(self):
        self.hand = Hand()