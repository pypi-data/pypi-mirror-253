from dataclasses import dataclass, field
import random
from playingcards.utils import concat_by_line
from typing import Union, Type
from collections import Counter

STANDARD_RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
_FRENCH_RANK_MAPPER = dict(zip(STANDARD_RANKS, range(1, 14)))
STANDARD_SUITS = ['s', 'h', 'c', 'd']
STANDARD_SUITS_PRETTY = ['♠', '♥', '♣', '♦']
_FRENCH_SUIT_MAPPER = dict(zip(STANDARD_SUITS, STANDARD_SUITS_PRETTY))


@dataclass(frozen=True, order=True)
class Rank:
    value: str = field(compare=False)
    num_value: int = None

    def __str__(self):
        return self.value

    def __sub__(self, other) -> int:
        return self.num_value - other.num_value

    def __bool__(self):
        """ Returns False when the value is an empty string. Otherwise True. """
        return bool(self.value)

    @classmethod
    def from_string(cls, string, french_deck=True, ace_high=True):
        """
        Produces a rank object from a string.
        :param string: The string of a rank, eg 'A'
        :param french_deck: bool, if true it'll automatically choose pretty suits
        :param ace_high: Whether the ace is the highest card in the deck
        :return: A rank object
        """
        if french_deck:
            num_r = _FRENCH_RANK_MAPPER[string] if string != 'A' else (14 if ace_high else 1)
            return Rank(string, num_r)
        else:
            return Rank(string)


@dataclass(frozen=True, order=True)
class Suit:
    """
    A class for custom suits
    :param : value. The desired value of the suit - s, h, c, d for a standard deck
    :param : pretty. Optional. A prettier representation of the suit - ♠, ♥, ♣, ♦ for a standard deck
    """
    value: str
    pretty: str = None

    def __str__(self):
        return self.pretty if self.pretty is not None else self.value

    def __bool__(self):
        """ Returns False when the value is an empty string. Otherwise True. """
        return bool(self.value)

    @classmethod
    def from_string(cls, string, french_deck=True):
        """
        Produces a suit object from a string.
        :param string: The string of a suit, eg 's'
        :param french_deck: bool, if true it'll automatically choose pretty suits
        :return: A suit object
        """
        if french_deck:
            return Suit(string, _FRENCH_SUIT_MAPPER[string])
        else:
            return Suit(string)


@dataclass(frozen=True, order=True)
class Card:
    rank: Rank
    suit: Suit = field(compare=False)

    def __str__(self):
        return str(self.rank) + str(self.suit)

    def str_value(self):
        return str(self.rank.value) + str(self.suit.value)

    @classmethod
    def from_string(cls, string, french_deck=True, ace_high=True):
        """
        Produces a card object from a string.
        :param string: The string of a card, eg 'As'
        :param french_deck: bool, if true it'll automatically choose pretty suits
        :param ace_high: Whether the ace is the highest card in the deck
        :return: A card object
        """
        r = string[0]
        s = string[1]

        return cls(Rank.from_string(r, french_deck=french_deck, ace_high=ace_high),
                   Suit.from_string(s, french_deck=french_deck))

    def ascii(self) -> str:
        """
        Creates an ASCII image of the playing card object.
        """
        return f"*- - -*\n|{self.suit}    |\n|  {self.rank}  |\n|   {self.suit} |\n*- - -*"

    def __eq__(self, other):
        return self.rank.value == other.rank.value and self.suit.value == other.suit.value

    def __bool__(self):
        """ Returns False when the card is empty. This means the Rank AND Suit is empty. Otherwise True. """
        return self.rank or self.suit


@dataclass
class CardCollection:
    # TODO: Continue adding from Poker Machin Learning - Board
    # TODO: Add checks for inputs. Running into issues when accidently specifying strings instead
    """
    A class for a collection of cards. Can be used for things like decks, hands, boards, etc
    """
    cards: list[Card] = field(default_factory=list)
    maximum: int = None
    ordered: bool = False
    reverse_order: bool = False

    def __post_init__(self):
        self._check_max_cards()
        self.order_cards()

    @property
    def rankings(self) -> list[Rank]:
        return [card.rank for card in self.cards]

    @property
    def rankings_unique(self) -> list[Rank]:
        used = set()
        return [x for x in self.rankings if x not in used and (used.add(x) or True)]

    @property
    def ranking_counts(self) -> Counter:
        return Counter(self.rankings)

    @property
    def ranking_counts_inv(self) -> dict[int, set[Rank]]:
        """
        The inverse of the ranking counts. Ie. shows which values are singles, pairs, triples etc.

        ranking_counts = Counter([8: 2, 4: 1, 2: 2])  --->   {2: {8, 2}, 1: {4}}
        """
        rci = {}
        for rank, count in self.ranking_counts.items():
            if count not in rci:
                rci[count] = set()
            rci[count].add(rank)
        return rci

    @property
    def suits(self) -> list[Suit]:
        return [card.suit for card in self.cards]

    @property
    def suit_counts(self) -> Counter:
        return Counter(self.suits)

    @property
    def suit_counts_inv(self) -> dict[int, set[Suit]]:
        """
        The inverse of the suit counts. Ie. shows which suits are singles, pairs, triples etc.

        suit_counts = Counter(['s': 2, 'h': 1, 'c': 2])  --->   {2: {'s', 'c'}, 1: {'h'}}
        """
        sci = {}
        for suit, count in self.suit_counts.items():
            if count not in sci:
                sci[count] = set()
            sci[count].add(suit)
        return sci

    def contains_same_card(self, other: Type['CardCollection']):
        return any([card in other.cards for card in self.cards])

    def add_cards(self, cards: Union[list[Card], 'CardCollection'], position=0, randomly=False):
        if not randomly:
            for card in cards:
                self.cards.insert(position, card)
                position += 1
        else:
            for card in cards:
                self.cards.insert(random.randint(0, len(self.cards)), card)
        self.order_cards()

    def remove_cards(self, cards: Union[list[Card], 'CardCollection']):  # Should add a by position option
        if isinstance(cards, CardCollection):
            cards = cards.cards
        for card in cards:
            if card in self.cards:
                self.cards.remove(card)

    def starts_with(self, sub_collection: 'CardCollection') -> bool:
        """
        Checks if the current collection starts with the sub-collection.
        :param sub_collection: The sub-collection to check
        :return: True if it starts with the sub-collection, False otherwise
        """
        return self.cards[:len(sub_collection)] == sub_collection.cards

    def filter_suit(self, suit: Suit):
        return CardCollection([card for card in self.cards if card.suit == suit])

    def normalize_suit_mapping(self, suit_order: tuple[Suit, Suit, Suit, Suit] = (
            Suit('s', '♠'),
            Suit('h', '♥'),
            Suit('c', '♣'),
            Suit('d', '♦')
    )) -> 'dict':
        """
        Returns a mapper for normalizing the suits of the collection
        :param suit_order:
        :return:
        """
        mapper = dict()
        for card in self.cards:
            if card.suit not in mapper:
                mapper[card.suit] = suit_order[len(mapper)]
        return mapper

    def change_suits(self, suit_mapper: dict[Suit, Suit], inplace=False) -> 'CardCollection':
        """
        Returns a new CardCollection with the suits changed according to the suit_mapper
        :param inplace: Whether to modify the current CardCollection or return a new one
        :param suit_mapper:
        :return:
        """
        if inplace:
            self.cards = [Card(card.rank, suit_mapper[card.suit]) for card in self.cards]
        else:
            return self.__class__([Card(card.rank, suit_mapper[card.suit]) for card in self.cards],
                                  maximum=self.maximum,
                                  ordered=self.ordered,
                                  reverse_order=self.reverse_order)

    def to_card_collection(self):
        return CardCollection(self.cards, maximum=self.maximum, ordered=self.ordered, reverse_order=self.reverse_order)

    def order_cards(self):
        if self.ordered:
            self.cards.sort(reverse=self.reverse_order)
            for i in range(len(self.cards) - 1):  # Put pairs in order of mosuit
                if self.ranking_counts[self.cards[i].rank] > 1 and self.cards[i].rank == self.cards[i+1].rank:
                    if self.suit_counts[self.cards[i].suit] < self.suit_counts[self.cards[i+1].suit]:
                        self.cards[i], self.cards[i+1] = self.cards[i+1], self.cards[i]

    def ascii(self):
        return concat_by_line([c.ascii() for c in self.cards], sep='  ')

    def _check_max_cards(self):
        if self.maximum is not None and len(self.cards) > self.maximum:
            raise ValueError("To many cards in collection")

    def __str__(self):
        return ' | '.join([str(card) for card in self.cards])

    def str_value(self, no_space=False):
        if no_space:
            return ''.join([card.str_value() for card in self.cards])
        else:
            return ' '.join([card.str_value() for card in self.cards])

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        return iter(self.cards)

    def __add__(self, other) -> 'CardCollection':
        # This just needs to return a card collection. If there's a higher level class that wants to return a different
        # type, then it can override this method
        # Does not maintain ordered, reverse_order, or maximum, as it not always clear what the desired behaviour is
        # If you want to maintain these, use the add_cards method
        if isinstance(other, Card):
            return CardCollection(self.cards + [other])
        elif isinstance(other, CardCollection):
            return CardCollection(self.cards + other.cards)  # Do not set maximum, ordered, or reverse_order, if this is needed, use the add_cards method
        else:
            raise TypeError(f"Cannot add {type(self)} to {type(other)}. CardCollections can only add to a Card or another CardCollection")

    def __radd__(self, other):  # Required to ensure sum works
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __getitem__(self, item):
        return self.cards[item]

    def __contains__(self, item: Card):
        return item in self.cards

    def __eq__(self, other):
        return set(self.cards) == set(other.cards)

    @classmethod
    def from_string(cls, string, french_deck=True):
        """
        Produces a CardCollection object from a string.
        :param string: The string of a card collection, eg 'AsKd', or 'As Kd'
        :param french_deck: bool, if true it'll automatically choose pretty suits
        :return: A CardCollection object
        """
        string = string.replace(' ', '')
        card_strings = [string[i:i+2] for i in range(0, len(string), 2)]
        return cls([Card.from_string(c, french_deck=french_deck) for c in card_strings])

    @classmethod
    def from_collections(cls, *card_collections: 'CardCollection'):
        # Can do cls(sum(card_collections).cards) as it tries to return instance of the first type when summing
        return cls([c for cc in card_collections for c in cc.cards])


class Deck(CardCollection):
    def __init__(self, cards=None, maximum=52):
        if cards is None:  # Generate a standard French deck if cards aren't specified
            cards = [
                Card(Rank(r, num_rank), Suit(s, pretty_suit))
                for s, pretty_suit in zip(STANDARD_SUITS, STANDARD_SUITS_PRETTY)
                for num_rank, r in enumerate(STANDARD_RANKS, start=1)
            ]
        super().__init__(cards, maximum=maximum)
        self._oringinal_deck = tuple(self.cards)  # tuple to avoid being changed (Card, Rank, and Suit are all frozen)

    def shuffle(self) -> None:
        """Shuffles the deck"""
        random.shuffle(self.cards)

    def reset(self, shuffle=False) -> None:
        """Add's all original cards back into the deck and optionally shuffles it"""
        self.cards = list(self._oringinal_deck)
        if shuffle:
            self.shuffle()

    def draw_top_n(self, n, collection_type: type = CardCollection):
        """
        Draws n cards from the top of the deck and returns the drawn cards. The Deck object will now have
        :param n: The number of cards to draw.
        :param collection_type: The class that the drawn cards form. For example you could put a 'Hand' class in here
        :return: The drawn cards, either of type CardCollection, or of inputted type
        """
        if len(self.cards) <= n-1:
            raise MaxCardsDrawn(f"Asked to draw {n} cards but there is only {len(self.cards)} left in deck")
        drawn_cards = self.cards[:n]
        self.cards = self.cards[n:]
        return collection_type(drawn_cards)

    @classmethod
    def from_ranks_suits(cls, ranks: list[Rank], suits: list[Suit]):
        return Deck([Card(r, s) for s in suits for r in ranks])


class MaxCardsDrawn(Exception):
    pass


class TooManyCards(Exception):
    pass


def is_f_card(card_str):
    """ Checks if a string is a valid french deck card """
    return card_str in Deck().str_value().split()


def main():
    cc = CardCollection.from_string('As7hKdKs5c7s5d5s')
    print(f'{cc.ranking_counts=}')
    print(f'{cc.ranking_counts_inv=}')
    print(f'{sorted(cc.rankings_unique, reverse=True)=}')


if __name__ == '__main__':
    main()
