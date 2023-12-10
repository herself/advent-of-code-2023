#!/usr/bin/python3

import sys
import re

line_parser = re.compile(r"(\w{3}).*(\w{3}).*(\w{3})")

instructions = sys.stdin.readline().strip().replace("L", "0").replace("R", "1")
sys.stdin.readline()

directions = {}
for line in sys.stdin:
    line_match = line_parser.match(line)
    directions[line_match.group(1)] = (line_match.group(2), line_match.group(3))

step = 0
current_node = "AAA"
while True:
    current_direction = int(instructions[step % len(instructions)])
    print("Going from {} to {}, choosing {}...".format(current_node, directions[current_node][current_direction], current_direction))
    current_node = directions[current_node][current_direction]
    step += 1
    if current_node == "ZZZ":
        print("Got there in {} steps!".format(step))
        break
