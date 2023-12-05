#!/usr/bin/python3

import sys
import re

game_power_sum = 0

for line in sys.stdin:
    print(line.strip())
    game_id = re.match(r'Game (\d+)', line).group(1)

    green_min_count = 0
    blue_min_count = 0
    red_min_count = 0

    for game_set in line.split(':')[1:][0].split(';'):
        print("  {}".format(game_set.strip()))

        green_count = re.search(r'(\d+) green', game_set)
        if green_count and int(green_count.group(1)) > green_min_count:
            print("  -- new green min found: {}".format(int(green_count.group(1))))
            green_min_count = int(green_count.group(1))

        red_count = re.search(r'(\d+) red', game_set)
        if red_count and int(red_count.group(1)) > red_min_count:
            print("  -- new red min found: {}".format(int(red_count.group(1))))
            red_min_count = int(red_count.group(1))

        blue_count = re.search(r'(\d+) blue', game_set)
        if blue_count and int(blue_count.group(1)) > blue_min_count:
            print("  -- new blue min found: {}".format(int(blue_count.group(1))))
            blue_min_count = int(blue_count.group(1))

    game_power = green_min_count * blue_min_count * red_min_count
    game_power_sum += game_power
    print("round power: {}\n".format(game_power))

print("Total game power: {}\n".format(game_power_sum))
