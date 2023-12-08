#!/usr/bin/python3

import sys
import re

from pprint import pprint
from itertools import count


def card_sort(char):
    order = "AKQJT98765432"
    return order.index(char)


def hand_sort(hand_info):
    order = "AKQJT98765432"
    return hand_info["type"] * 10000000000 \
        + order.index(hand_info["hand"][0]) * 100000000 \
        + order.index(hand_info["hand"][1]) * 1000000 \
        + order.index(hand_info["hand"][2]) * 10000 \
        + order.index(hand_info["hand"][3]) * 100 \
        + order.index(hand_info["hand"][4]) * 1


number_catcher = re.compile(r"(\d+)")
card_types = []
card_types.append(re.compile(r"([AKQJT98765432])\1{4}"))  # five of a kind
card_types.append(re.compile(r"([AKQJT98765432])\1{3}"))  # four of a kind
card_types.append(re.compile(r"([AKQJT98765432])\1{2}([^\1])\2|([AKQJT98765432])\3([^\3])\4{2}"))  # full house
card_types.append(re.compile(r"([AKQJT98765432])\1{2}"))  # three of a kind
card_types.append(re.compile(r"([AKQJT98765432])\1.*?([^\1])\2|([AKQJT98765432])\3.*?([^\3])\4"))  # two pair
card_types.append(re.compile(r"([AKQJT98765432])\1"))  # one pair
card_types.append(re.compile(r".*"))  # high card


hands_input = [x for x in sys.stdin.read().strip().split()]
hands_dealt = [{"hand": x, "value": int(y)} for x, y in zip(hands_input[0::2], hands_input[1::2])]

for hand_info in hands_dealt:
    for i, card_type in enumerate(card_types):
        if card_type.search("".join(sorted(hand_info["hand"], key=card_sort))):
            hand_info["type"] = i
            break

original_order = count()


pprint(hands_dealt)
print()
hands_sorted = sorted(hands_dealt, key=hand_sort)
pprint(hands_sorted)
print()

total_winnings = 0
for i, hand_info in enumerate(reversed(hands_sorted)):
    total_winnings += (i + 1) * hand_info["value"]

print("Total winnings: {}".format(total_winnings))
