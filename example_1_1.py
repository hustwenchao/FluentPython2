import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)

deck: FrenchDeck = FrenchDeck()
print(len(deck))

print(deck[0])
print(deck[-1])

# 随机抽取一张牌
from random import choice

print(choice(deck))

for card in deck:
    print(card)

for card in reversed(deck):
    print(card)

print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(cardX) -> int:
    rank_value = FrenchDeck.ranks.index(cardX.rank)
    return rank_value * len(suit_values) + suit_values[cardX.suit]


for card in sorted(deck, key=spades_high):
    print(card)
