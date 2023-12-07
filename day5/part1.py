#!/usr/bin/python3

import sys
import re

number_catcher = re.compile(r"(\d+)")
ingredient_map_ranges = {}
ingredient_mappings = {}

seed_line = sys.stdin.readline()
seeds_transposed = {"original": [int(x) for x in number_catcher.findall(seed_line)]}

print("Got seed list: {}".format(seeds_transposed["original"]))
# get rid of empty line
sys.stdin.readline()

stages_list = ["original"]

while True:
    map_line = sys.stdin.readline()
    # no more input at all
    if len(map_line) == 0:
        break

    map_name = re.match(r"(\S+) map:", map_line).group(1)
    print("Map name: {}".format(map_name))
    stages_list.append(map_name)

    ingredient_map_ranges[map_name] = []
    for line in sys.stdin:
        # end of range lists
        if len(line.strip()) == 0:
            break
        [destination, source, length] = number_catcher.findall(line)
        ingredient_map_ranges[map_name].append({"destination": int(destination), "source": int(source), "length": int(length)})

print("\nIngredient map ranges: {}".format(ingredient_map_ranges))

for key, range_list in ingredient_map_ranges.items():
    print("Analyzing {}".format(key))
    ingredient_mappings[key] = {}
    for range_item in range_list:
        print(range_item)
        for i in range(range_item["length"]):
            ingredient_mappings[key][range_item["source"] + i] = range_item["destination"] + i

print("\nIngredient mappings: {}\n".format(ingredient_mappings))

for step, used_map in enumerate(stages_list[1:]):
    print(used_map)
    seeds_transposed[used_map] = []
    for i in range(len(seeds_transposed["original"])):
        try:
            seeds_transposed[used_map].append(
                ingredient_mappings[used_map][
                    seeds_transposed[stages_list[step]][i]
                ])
        except KeyError:
            seeds_transposed[used_map].append(seeds_transposed[stages_list[step]][i])
    print(seeds_transposed)

print("\nLowest location number: {}".format(min(seeds_transposed["humidity-to-location"])))
