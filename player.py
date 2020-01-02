from playerBase import PlayerBase
from playerActions import Action


class Player(PlayerBase):
    def __init__(self, balance, name = "John Doe"):
        super().__init__(name)
        print(f'Player: "{name}" is joining with a balance: ({balance})')
        self.balance = balance
    
    def play(self, action):
        """
        Not needed?
        Hit or stand
        """


    
