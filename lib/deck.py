class Deck:
  def __init__(self, cards):
    self.cards = cards

  def value_of_card_at(self, index):
    if self.cards != [] and index >= len(self.cards) and len(self.cards) > 1:
      return self.cards[-1].value
    elif self.cards != []:
      return self.cards[index].value
    elif self.cards == []:
      return 0


  def high_ranking_cards(self):
    high_cards = []
    for card in self.cards:
      if card.value > 10:
        high_cards.append(card)
    return high_cards


  def percent_high_ranking(self):
    return len(self.high_ranking_cards()) / len(self.cards)

  def remove_card(self):
    self.cards.pop(0)

  def add_card(self, card):
    self.cards.append(card)