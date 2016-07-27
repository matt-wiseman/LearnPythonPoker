from models import Card


def create_deck():
    """Create a list of playing cards in the database"""
    suits = [suit[0] for suit in Card.SUIT_CHOICES]
    ranks = [rank[0] for rank in Card.RANK_CHOICES]

    cards = [Card(suit=suit, rank=rank) for rank in ranks for suit in suits]
    Card.objects.bulk_create(cards)
