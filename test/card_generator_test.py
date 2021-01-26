import unittest
import sys
sys.path.append('.')

from lib.card_generator import CardGenerator


class TestCardGenerator(unittest.TestCase):
  def setUp(self):
    self.generator = CardGenerator()

  def test_it_exists(self):
    assert type(self.generator) == CardGenerator
    assert len(self.generator.shuffled_deck) == 52
    assert len(self.generator.deck1) == 26
    assert len(self.generator.deck2) == 26