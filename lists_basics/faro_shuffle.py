deck_of_cards = input().split()
number_of_shuffles = int(input())

for shuffe in range(number_of_shuffles):
    final_deck = []
    middle_of_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle_of_deck]
    right_part = deck_of_cards[middle_of_deck:]
    for index in range(len(left_part)):
        final_deck.append(left_part[index])
        final_deck.append(right_part[index])
    deck_of_cards = final_deck

print(deck_of_cards)
