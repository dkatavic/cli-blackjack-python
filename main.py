from deck import Deck
from player import Player
from dealer import Dealer
from playerActions import Action
# Only Hit and Stay
# Player prvo. Hit ili 21

# Game class?

def finish_round(player, bet, win):
    if win:
        player.balance += bet
        print(f'You won the round. Balance: {player.balance}')
    else:
        player.balance -= bet
        print(f'You lost the round. Balance: {player.balance}')

def play_round(player, dealer):
    # TODO: Check balance
    betting_amout = int(input(f'Hello {player.name} ({player.balance}c). Input betting amount: '))
    deck = Deck()
    deck.shuffle()
    player.reset_hand()
    dealer.reset_hand()
    # 2 cards for a player
    player.add_card(deck.draw())
    player.add_card(deck.draw())

    player_playing = True
    while player_playing:
        print(f'Player {player.name} has hand ({str(player.hand)}). Score: {player.get_score()}')
        decision = None
        while decision not in list(Action):
            decision_str = (input(f'Hit ({Action.HIT.value}) or Stand ({Action.STAND.value})?: '))
            try:
                decision = Action(int(decision_str))
            except:
                print(f'{decision_str} is not a valid Action')
        
        if decision == Action.STAND:
            print(f'Standing! Score: {player.get_score()}')
            player_playing = False
        else:
            player.add_card(deck.draw())
            if player.get_score() == 21:
                print('BLACKJACK!!!!')
                player_playing = False
                return finish_round(player, betting_amout, True)
            elif player.get_score() > 21:
                print(f'Busted! Score: {player.get_score()}')
                player_playing = False
                # TODO: Exit to beginning or call end round
                return finish_round(player, betting_amout, False)
    dealer_playing = True
    dealer.add_card(deck.draw())
    dealer.add_card(deck.draw())
    while dealer_playing:
        print(f'Dealer {dealer.name} has hand ({str(dealer.hand)}). Score: {dealer.get_score()}')
        if dealer.get_score() > 21:
            # BUST
            print(f'Dealer busted! Score: {dealer.get_score()}')
            return finish_round(player, betting_amout, True)
        if dealer.get_score() == 21:
            print('Dealer Got blackjack!')
            return finish_round(player, betting_amout, False)
        if dealer.get_score() > player.get_score():
            print(f'Dealer won with score {dealer.get_score()} vs {player.get_score()}')
            return finish_round(player, betting_amout, False)
        else:
            dealer.add_card(deck.draw())
    
            




def main():

    player = Player(balance = 100, name = "John")
    dealer = Dealer(name = "Give me monnies")
    """
    Gameplan:
    * start partije
    * odredi betting amout
    * drawaj 2 karte (PlayerHand za ovo, da moze kalkulirat totalni value i tako)
    * reci status
    * input akciju
    * stand or hit
    * zatim dealer
    * drawa dok ne bude veci od playera, dok ne hita 21 ili dok ne busta
    * slijedeci turn
    """
    playing_game = True
    while playing_game:
        play_round(player, dealer)

        
if __name__ == "__main__":
    main()