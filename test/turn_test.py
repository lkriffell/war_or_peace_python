import unittest
import sys
sys.path.append('.')

from lib.card import Card
from lib.deck import Deck
from lib.player import Player
from lib.turn import Turn


class TestTurn(unittest.TestCase):
  def setUp(self):
    card_one = Card("Heart", "5", 5)
    card_two = Card("Diamond", "Jack",11)
    card_three = Card("Spade", "7", 7)
    card_four = Card("Spade", "Ace", 14)
    cards = [card_one, card_two, card_three, card_four]
    self.deck = Deck(cards)
    self.player1 = Player("John", self.deck)
    card_five = Card("Heart", "8", 8)
    card_six = Card("Diamond", "Jack",11)
    card_seven = Card("Spade", "3", 3)
    card_eight = Card("Club", "Queen", 12)
    cards2 = [card_five, card_six, card_seven, card_eight]
    self.deck2 = Deck(cards2)
    self.player2 = Player("John", self.deck2)
    self.turn = Turn(self.player1, self.player2)
    
  def test_it_exists(self):
    assert type(self.turn) == Turn
    assert type(self.turn.player1) == Player
    assert type(self.turn.player2) == Player

  def test_turn_type_basic(self):
    assert self.turn.turn_type() == 'Basic'

  def test_turn_type_war(self):
    self.player2.deck.cards.insert(0, Card("Spade", "5", 5))
    assert self.turn.turn_type() == 'War!'

  def test_turn_type_mad(self):
    self.player2.deck.cards.insert(0, Card("Spade", "5", 5))
    self.player1.deck.cards.insert(1, Card("Diamond", "7", 7))
    assert self.turn.turn_type() == 'MAD!'

  def test_pile_those_cards(self):
    self.turn.pile_those_cards(self.turn.player1.deck.cards, self.turn.player2.deck.cards)
    assert len(self.turn.spoils) == 2
    assert len(self.turn.player1.deck.cards) == 3
    assert len(self.turn.player2.deck.cards) == 3

  def test_winner_basic(self):
    assert self.turn.turn_type() == 'Basic'
    self.turn.pile_those_cards(self.turn.player1.deck.cards, self.turn.player2.deck.cards)
    assert self.turn.winner() == self.player2

  def test_winner_war(self):
    self.player2.deck.cards.insert(0, Card("Spade", "5", 5))
    assert self.turn.turn_type() == 'War!'
    self.turn.pile_those_cards(self.turn.player1.deck.cards, self.turn.player2.deck.cards)
    assert self.turn.winner() == self.player2

  def test_winner_mad(self):
    self.player2.deck.cards.insert(0, Card("Spade", "5", 5))
    self.player1.deck.cards.insert(1, Card("Diamond", "7", 7))
    assert self.turn.turn_type() == 'MAD!'
    assert self.turn.winner() == 'No Winner'
  
  def test_awards_spoils(self):
    self.turn.pile_those_cards(self.turn.player1.deck.cards, self.turn.player2.deck.cards)
    self.turn.award_spoils()
    assert len(self.turn.player2.deck.cards) == 5


if __name__ == '__main__':
    unittest.main()