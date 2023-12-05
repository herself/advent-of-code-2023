#!/usr/bin/python3

import sys
import re

RED_MAX_COUNT = 12
GREEN_MAX_COUNT = 13
BLUE_MAX_COUNT = 14

valid_id_sum = 0

for line in sys.stdin:
    print(line.strip())
    game_id = re.match(r'Game (\d+)', line).group(1)
    game_valid = True
    for game_set in line.split(':')[1:][0].split(';'):
        print("  {}".format(game_set.strip()))

        green_count = re.search(r'(\d+) green', game_set)
        if green_count and int(green_count.group(1)) > GREEN_MAX_COUNT:
            print("  -- WRONG GREEN")
            game_valid = False

        red_count = re.search(r'(\d+) red', game_set)
        if red_count and int(red_count.group(1)) > RED_MAX_COUNT:
            print("  -- WRONG RED")
            game_valid = False

        blue_count = re.search(r'(\d+) blue', game_set)
        if blue_count and int(blue_count.group(1)) > BLUE_MAX_COUNT:
            print("  -- WRONG BLUE")
            game_valid = False

    if game_valid:
        valid_id_sum += int(game_id)

print("\nSum of valid IDs: {}".format(valid_id_sum))
