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

for step, used_map in enumerate(stages_list[1:]):
    print(used_map)
    seeds_transposed[used_map] = []
    for i in range(len(seeds_transposed["original"])):
        current_seed = seeds_transposed[stages_list[step]][i]
        print("current: {} ({})".format(current_seed, i))
        for range_item in ingredient_map_ranges[used_map]:
            range_start = range_item["source"]
            range_finish = range_item["source"] + range_item["length"] - 1

            print("Checking range {}, start: {}, finish: {}".format(range_item, range_start, range_finish))
            if current_seed >= range_start and current_seed <= range_finish:
                print("Seed transposed! {} <= {} <= {}".format(range_start, current_seed, range_finish))
                seeds_transposed[used_map].append(range_item["destination"] + (current_seed - range_start))

        if len(seeds_transposed[used_map]) == i:
            seeds_transposed[used_map].append(current_seed)

print("\nLowest location number: {}".format(min(seeds_transposed["humidity-to-location"])))
