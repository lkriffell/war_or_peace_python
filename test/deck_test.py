import unittest
import sys
sys.path.append('.')

from lib.card import Card
from lib.deck import Deck

class TestCards(unittest.TestCase):
  def setUp(self):
    self.card_one = Card("Hearts", "5", 5)
    self.card_two = Card("Diamonds", "Jack",11)
    self.card_three = Card("Spades", "7", 7)
    self.card_four = Card("Spades", "Ace", 14)
    cards = [self.card_one, self.card_two, self.card_three, self.card_four]
    self.deck = Deck(cards)

  def test_it_exists(self):
    assert type(self.deck) == Deck
    assert type(self.deck.cards[0]) == Card

  def test_rank_of_card_at(self):
    assert self.deck.rank_of_card_at(0) == '5'
    assert self.deck.rank_of_card_at(1) == 'Jack'
    assert self.deck.rank_of_card_at(2) == '7'

  def test_high_ranking_cards(self):
    assert self.deck.high_ranking_cards() == [self.card_two, self.card_four]
  
  def test_percent_high_ranking(self):
    assert self.deck.percent_high_ranking() == 0.5

  def test_remove_card(self):
    self.deck.remove_card()
    assert len(self.deck.cards) == 3

  def test_add_card(self):
    new_card = Card("Hearts", "King", 13)
    self.deck.add_card(new_card)
    assert len(self.deck.cards) == 5

if __name__ == '__main__':
    unittest.main()