class Deck:
  def __init__(self, cards):
    self.cards = cards

  def rank_of_card_at(self, index):
    return self.cards[index].rank

  def high_ranking_cards(self):
    return map(lambda card: card.rank > 10, self.cards)

  def percent_high_ranking(self):
    return len(high_ranking_cards(self)) / len(self.cards)