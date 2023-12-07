#!/usr/bin/python3

import sys
import re

number_catcher = re.compile(r"(\d+)")
total_score = 0

for line in sys.stdin:
    print(line.strip())

    card_id = re.match(r"Card\s+(\d+)", line).group(1)
    print(card_id)

    [win_numbers, our_numbers] = line.strip().split(':')[1:][0].split("|")
    win_numbers_set = set(number_catcher.findall(win_numbers))
    our_numbers_set = set(number_catcher.findall(our_numbers))
    winning_number_count = len(win_numbers_set.intersection(our_numbers_set))

    print("{}, total winning: {}".format(win_numbers_set.intersection(our_numbers_set), winning_number_count))
    if winning_number_count > 0:
        total_score += 2 ** (winning_number_count - 1)

print("Total score: {}".format(total_score))
