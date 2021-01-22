import unittest
import sys
sys.path.append('.')

from lib.card import Card


class TestCards(unittest.TestCase):
  def test_it_exists(self):
    new_card = Card("Hearts", "5", 5)
    assert type(new_card) == Card
    assert new_card.suit == 'Hearts'
    assert new_card.rank == '5'
    assert new_card.value == 5

if __name__ == '__main__':
    unittest.main()