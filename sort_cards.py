def sort_cards(stuff):
    """Sorts a list of cards by ascending values."""
    cards = {
    'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13
    }
    return sorted(stuff, key=cards.get)
