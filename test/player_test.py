import unittest
import sys
sys.path.append('.')

from lib.card import Card
from lib.deck import Deck
from lib.player import Player


class TestCards(unittest.TestCase):
  def setUp(self):
    card_one = Card("Heart", "5", 5)
    card_two = Card("Diamond", "Jack",11)
    card_three = Card("Spade", "7", 7)
    card_four = Card("Spade", "Ace", 14)
    cards = [card_one, card_two, card_three, card_four]
    self.deck = Deck(cards)
    self.player = Player("John", self.deck)
    
  def test_it_exists(self):
    assert type(self.player) == Player
    assert self.player.name == 'John'
    assert self.player.deck == self.deck

  def test_has_lost(self):
    assert self.player.has_lost() == False
    self.player.deck.remove_card()
    self.player.deck.remove_card()
    assert self.player.has_lost() == False
    self.player.deck.remove_card()
    self.player.deck.remove_card()
    assert self.player.has_lost() == True

if __name__ == '__main__':
    unittest.main()