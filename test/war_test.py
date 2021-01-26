import unittest
import sys
sys.path.append('.')

from contextlib import contextmanager
from war import War
from lib.player import Player

class TestWar(unittest.TestCase):
  def test_it_exists_and_can_be_won(self):
    self.war = War()
    assert type(self.war) == War
    assert type(self.war.winner_of_game()) == Player



