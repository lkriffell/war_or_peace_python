import unittest
import sys
sys.path.append('.')

from war import War
from lib.player import Player

class TestWar(unittest.TestCase):
  def setUp(self):
    self.war = War()

  def test_it_exists(self):
    assert type(self.war) == War
  
  def test_it_can_be_won(self):
    self.war.start()
    assert type(self.war.winner_of_game()) == Player


