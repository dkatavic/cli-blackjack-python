from playerBase import PlayerBase
from playerActions import Action

class Dealer(PlayerBase):
    def __init__(self, name = "Dealer"):
        super().__init__(name)
        print(f'Dealer: "{name}" is joining')
    
    def play(self, action):
        """
        Not needed?
        Hit or stand
        """
