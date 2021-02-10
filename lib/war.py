from lib.card_generator import CardGenerator
from lib.player import Player
from lib.turn import Turn
from lib.deck import Deck

class War:
  def __init__(self):
    self.player1 = ''
    self.player2 = ''
    self.turn_count = 0
    self.create_players()

  def create_players(self):
    generator = CardGenerator()
    self.player1 = Player("Darrel", Deck(generator.deck1))
    self.player2 = Player("Phillis", Deck(generator.deck2))

  def new_turn(self):
    self.turn_count += 1
    return Turn(self.player1, self.player2)
  
  def winner_of_game(self):
    if len(self.player1.deck.cards) == 0:
      return self.player2
    elif len(self.player2.deck.cards) == 0:
      return self.player1

  def start(self):
    print('Welcome to War! (or Peace) This game will be played with 52 cards.')
    print('The players today are %s and %s.'%(self.player1.name, self.player2.name))
    go = input("Type 'GO' to start the game!")
    if go.lower() == 'go':
      while self.player1.has_lost() == False and self.player2.has_lost() == False and self.turn_count < 1000000:
        turn = self.new_turn()
        winner = turn.winner()
        if turn.turn_type() == 'Basic':
          turn.pile_those_cards(self.player1.deck.cards, self.player2.deck.cards)
          turn.award_spoils()
          print("turn %d: %s won 2 cards!"%(self.turn_count, winner.name))
        elif turn.turn_type() == 'War!':
          if winner == None:
            import ipdb; ipdb.set_trace()
          turn.pile_those_cards(self.player1.deck.cards, self.player2.deck.cards)
          turn.award_spoils()
          print("turn %d: War! %s won 6 cards!"%(self.turn_count, winner.name))
        elif winner == 'No Winner':
          turn.pile_those_cards(self.player1.deck.cards, self.player2.deck.cards)
          print("turn %d: *Mutaully Assured Destruction* 6 cards removed from play"%(self.turn_count))
      if self.turn_count == 1000000:
        print('---- DRAW ----')
      else:
        winner = self.winner_of_game()
        print("And the winner is: %s!"%(winner.name))
    else:
      print('ok dont play...')