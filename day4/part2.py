#!/usr/bin/python3

import sys
import re

number_catcher = re.compile(r"(\d+)")
card_deck = []
total_cards = 0

for line in sys.stdin:
    print(line.strip())

    card_id = re.match(r"Card\s+(\d+)", line).group(1)

    [win_numbers, our_numbers] = line.strip().split(':')[1:][0].split("|")
    win_numbers_set = set(number_catcher.findall(win_numbers))
    our_numbers_set = set(number_catcher.findall(our_numbers))
    winning_number_count = len(win_numbers_set.intersection(our_numbers_set))

    card_deck.append({"card_count": 1, "win_count": winning_number_count})

    print("card #{}, total winning: {}\n".format(card_id, winning_number_count))

for card_pos, card_data in enumerate(card_deck):
    print("card position: {}, data: {}".format(card_pos, card_data))
    for i in range(card_data["win_count"]):
        card_deck[card_pos + i + 1]["card_count"] += card_deck[card_pos]["card_count"]
    total_cards += card_data["card_count"]

print("\nTotal number of scratchcards: {}".format(total_cards))
