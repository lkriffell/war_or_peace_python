from lib.player import Player

class Turn:
  def __init__(self, player1, player2):
    self.player1 = player1
    self.player2 = player2
    self.spoils = []

  def turn_type(self):
    if self.player1.deck.value_of_card_at(0) != self.player2.deck.value_of_card_at(0):
      return 'Basic'
    elif self.player1.deck.value_of_card_at(0) == self.player2.deck.value_of_card_at(0) and len(self.player1.deck.cards) >= 3 and len(self.player2.deck.cards) >= 3 and self.player1.deck.value_of_card_at(2) != self.player2.deck.value_of_card_at(2):
      return 'War!'
    elif len(self.player1.deck.cards) > 1 and len(self.player2.deck.cards) > 1:
      if self.player1.deck.value_of_card_at(0) == self.player2.deck.value_of_card_at(0) and self.player1.deck.value_of_card_at(2) == self.player2.deck.value_of_card_at(2):
        return 'MAD!'

  def winner(self):
    if self.turn_type() == 'Basic':
      if self.player1.deck.value_of_card_at(0) > self.player2.deck.value_of_card_at(0):
        return self.player1
      elif self.player1.deck.value_of_card_at(0) < self.player2.deck.value_of_card_at(0):
        return self.player2
    elif self.turn_type() == 'War!':
      if len(self.player1.deck.cards) == 1:
        return self.player2
      elif len(self.player2.deck.cards) == 1:
        return self.player1
      elif self.player1.deck.value_of_card_at(2) > self.player2.deck.value_of_card_at(2):
        return self.player1
      elif self.player1.deck.value_of_card_at(2) < self.player2.deck.value_of_card_at(2):
        return self.player2
    else:
      self.spoils = []
      return 'No Winner'

  def pile_those_cards(self, p1_cards, p2_cards):
    if self.turn_type() == 'Basic':
      num_cards = 1
    else:
      num_cards = 2
    for i in range(num_cards):
      if len(p1_cards) > 0:
        self.spoils.append(p1_cards[0])
        self.player1.deck.remove_card()
      if len(p2_cards) > 0:
        self.spoils.append(p2_cards[0])
        self.player2.deck.remove_card()

  def award_spoils(self):
    if type(self.winner()) == Player:
      for card in self.spoils:
        self.winner().deck.add_card(card)
