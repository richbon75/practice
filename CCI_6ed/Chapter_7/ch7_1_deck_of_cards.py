"""Design the data structures for a generic deck of cards. Explain how
you would subclass the data structures to implement blackjack."""

from random import randint

class Deck(object):
    """A Deck of Cards"""

    def __init__(self):
        """create an empty deck of cards"""
        self.deck = list()
        # Return pile. Cards back in the deck, but not available for dealing.
        self.return_pile = list()

    def __len__(self):
        """How many cards in the deck available to deal?"""
        return len(self.deck)

    def print(self):
        """Print out the whole deck"""
        for card in self.deck:
            print(card)

    def deal(self):
        """Deals a card off the top of the deck."""
        if self.deck:
            return self.deck.pop()
        if not self.return_pile:
            return None
        # If the dealing deck is empty, return the discard
        # pile to play and shuffle the deck. Then deal.
        self.shuffle()
        return self.deck.pop()

    def return_card(self, card):
        """Places a card into the return pile"""
        self.return_pile.append(card)

    def populate(self, iterable):
        """Put a whole bunch of cards into the deck."""
        self.deck += [card for card in iterable]

    def shuffle(self):
        """Shuffles the cards in the deck by randomly swapping cards.
        Also returns any cards from the return deck back to the dealable deck."""
        self.deck += self.return_pile
        self.return_pile = list()
        for _ in range(1000):
            i = randint(0, len(self.deck)-1)
            j = randint(0, len(self.deck)-1)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]

class Card(object):
    """A card."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class PlayingCard(Card):
    """A standard playing card"""

    card_suits = ('Diamonds', 'Hearts', 'Spades', 'Clubs')
    card_values = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')

    def __init__(self, suit, value):
        super().__init__(value)
        self.suit = suit

    def __str__(self):
        return '{} of {}'.format(self.value, self.suit)

    @classmethod
    def all_cards(self):
        """Iterator returning every possible card in the deck."""
        for i in range(len(__class__.card_suits) * len(__class__.card_values)):
            suit = __class__.card_suits[i // len(__class__.card_values)]
            value = __class__.card_values[i % len(__class__.card_values)]
            yield __class__(suit=suit, value=value)

    @classmethod
    def full_deck(self):
        """Return a full deck of playing cards."""
        deck = Deck()
        deck.populate(__class__.all_cards())
        return deck            

class BlackJackHand(object):
    """Holds a hand of cards for Blackjack. Keeps a reference to
    the deck being used for play, so cards can be dealt from and
    returned to the deck."""
    
    def __init__(self, deck):
        self.hand = list()
        self.deck = deck

    def __str__(self):
        if self.hand:
            return ', '.join([str(card) for card in self.hand])
        else:
            return 'Empty hand'

    def hit(self):
        """Deal a card from the deck to this hand."""
        self.hand.append(deck.deal())
        print(self)
        scores = self.scores()
        if len(scores) == 0:
            print('BUSTED')
        elif len(self.hand) == 2 and 21 in scores:
            print('BLACKJACK!')
        elif 21 in scores:
            print('WINNER!')                  
        else:
            print(scores)

    def empty(self):
        """Returns all cards in the hand to the deck."""
        while self.hand:
            deck.return_card(self.hand.pop())

    def scores(self):
        """Returns set of valid score interpretations."""
        scores = [0]
        for card in self.hand:
            if card.value in ('J', 'Q', 'K'):
                scores = [score + 10 for score in scores]
            elif card.value == 'A':
                scores = [score + 1 for score in scores] + [score + 11 for score in scores]
            else:
                scores = [score + card.value for score in scores]
        return set([score for score in scores if score <= 21])

if __name__ == "__main__":
    deck = PlayingCard.full_deck()
    deck.shuffle()
    alfie = BlackJackHand(deck)
    alfie.hit()
    alfie.hit()
    alfie.hit()
    alfie.empty()
    

    
        
        
    
