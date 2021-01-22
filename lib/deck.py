class Deck:
  def __init__(self, cards):
    self.cards = cards

  def rank_of_card_at(self, index):
    return self.cards[index].rank

  def high_ranking_cards(self):
    # result = map(lambda card: card.value > 10, self.cards)
    # return list(result)
    high_cards = []
    for card in self.cards:
      if card.value > 10:
        high_cards.append(card)
    return high_cards


  def percent_high_ranking(self):
    return len(self.high_ranking_cards()) / len(self.cards)

  def remove_card(self):
    self.cards.pop(1)

  def add_card(self, card):
    self.cards.append(card)