values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['♠', '♡', '♢', '♣']
cards = [value + suit for value in values for suit in suits]

print(cards)