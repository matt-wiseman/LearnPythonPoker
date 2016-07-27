from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Card(models.Model):
    """Representation of a playing card.

    Attributes:
        rank -- Integer representing card value.
        suit -- Integer representing card suit.
    """
    RANK_CHOICES = (
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
        (6, 'Six'),
        (7, 'Seven'),
        (8, 'Eight'),
        (9, 'Nine'),
        (10, 'Ten'),
        (11, 'Jack'),
        (12, 'Queen'),
        (13, 'King'),
        (14, 'Ace'),
    )
    SUIT_CHOICES = (
        (0, "Spades"),
        (1, "Diamonds"),
        (2, "Clubs"),
        (3, "Hearts"),
    )

    rank = models.PositiveSmallIntegerField(choices=RANK_CHOICES)
    suit = models.PositiveSmallIntegerField(choices=SUIT_CHOICES)

    def __str__(self):
        return "{} of {}".format(
            self.get_rank_display(),
            self.get_suit_display(),
        )


class Hand(models.Model):
    """Representation of a poker hand.

    Attributes:
        cards -- ManyToManyField representing cards in the hand.
        player -- OneToOneField reference to player holding the hand.
        table -- OneToOneField reference to table where the hand is in play.

    Beware: Attempting to manipulate the cards attribute before an initial save
    of the model will cause a Recursion error. This happens with all ManyToMany
    fields.
    """

    cards = models.ManyToManyField(Card)
    player = models.OneToOneField("Player")
    table = models.OneToOneField("Table")

    def __str__(self):
        hand_str = ", ".join(map(str, self.cards.all()))
        return "Cards: {}\nHeld by {} at Table {}".format(
            hand_str, str(self.player), self.table.pk
        )


class Player(models.Model):
    """Player data associated with User account.

    Attributes:
        user -- OneToOneField reference to the django User.
        bankroll -- PositiveInteger containing the users current monies.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bankroll = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.user)


class Table(models.Model):
    """Representation of a poker table.

    Attributes:
        players -- ManyToManyField referencing current players seated
    at the table.
        pot -- PositiveInteger containing the current pot at the table.
    """

    players = models.ManyToManyField(Player)
    pot = models.PositiveIntegerField(default=0)

    def __str__(self):
        player_str = ", ".join(map(str, self.players.all()))
        return "Players: {}\nPot: {}".format(player_str, self.pot)
