from lib.player import Player

class Turn:
  def __init__(self, player1, player2):
    self.player1 = player1
    self.player2 = player2
    self.spoils = []

  def turn_type(self):
    if self.player1.deck.rank_of_card_at(0) == self.player2.deck.rank_of_card_at(0) and self.player1.deck.rank_of_card_at(2) == self.player2.deck.rank_of_card_at(2):
      return 'MAD!'
    elif self.player1.deck.rank_of_card_at(0) == self.player2.deck.rank_of_card_at(0):
      return 'War!'
    else:
      return 'Basic'

  def winner(self):
    if self.turn_type() == 'Basic':
      if self.player1.deck.rank_of_card_at(0) > self.player2.deck.rank_of_card_at(0):
        return self.player1
      elif self.player1.deck.rank_of_card_at(0) < self.player2.deck.rank_of_card_at(0):
        return self.player2
    elif self.turn_type() == 'War!':
      if self.player1.deck.rank_of_card_at(2) > self.player2.deck.rank_of_card_at(2):
        return self.player1
      elif self.player1.deck.rank_of_card_at(2) < self.player2.deck.rank_of_card_at(2):
        return self.player2
    else:
      self.spoils = []
      return 'No Winner'

  def pile_those_cards(self, p1_cards, p2_cards):
    if turn_type() == 'Basic':
      num_cards = 1
    else:
      num_cards = 2
    for i in range(num_cards):
      self.spoils.append(p1_cards[0])
      self.player1.deck.remove_card()
      self.spoils.append(p2_cards[0])
      self.player2.deck.remove_card()

  def award_spoils(self):
    if type(self.winner()) == Player:
      for card in self.spoils:
        self.winner().deck.add_card(card)
