import unittest
import sys
sys.path.append('.')

from lib.card import Card
from lib.deck import Deck

class TestCards(unittest.TestCase):
  def setUp(self):
    cards = []
    self.card_one = cards.append(Card("Hearts", "5", 5))
    self.card_two = cards.append(Card("Diamonds", "Jack",11))
    self.card_three = cards.append(Card("Spades", "7", 7))
    self.card_four = cards.append(Card("Spades", "Ace", 14))
    self.new_deck = Deck(cards)

  def test_it_exists(self):
    assert type(self.new_deck) == Deck
    assert type(self.new_deck.cards[0]) == Card

  def test_rank_of_card_at(self):
    assert self.new_deck.rank_of_card_at(0) == '5'
    assert self.new_deck.rank_of_card_at(1) == 'Jack'
    assert self.new_deck.rank_of_card_at(2) == '7'

  def test_high_ranking_cards(self):
    self.new_deck.high_ranking_cards == [self.card_two, self.card_four]
  
  def test_percent_high_ranking(self):
    self.new_deck.percent_high_ranking == .5


if __name__ == '__main__':
    unittest.main()