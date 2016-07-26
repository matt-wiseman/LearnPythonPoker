from __future__ import unicode_literals

from django.db import models


class Card(models.Model):
    """Representation of a playing card."""
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
