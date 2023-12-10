#!/usr/bin/python3

import sys
import itertools

PIPE_TYPES = {
    "|": ((-1, 0), (1, 0)),
    "-": ((0, -1), (0, 1)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((1, 0), (0, -1)),
    "F": ((1, 0), (0, 1)),
    "S": ((1, 0), (0, 1), (-1, 0), (0, -1)),
}


def find_adjacent_pipes(map_values, check_position):
    adjacent_positions = []
    print("> Checking position {} = '{}' for adjacent pipes to follow".format(check_position, map_values[check_position[0]][check_position[1]]))
    for (adjustment_l, adjustment_c) in PIPE_TYPES[map_values[check_position[0]][check_position[1]]]:
        pos_l = check_position[0] + adjustment_l
        pos_c = check_position[1] + adjustment_c
        sym_to_check = map_values[pos_l][pos_c]
        print(" > Checking option {}/{} = sym '{}'".format(adjustment_l, adjustment_c, sym_to_check))
        if sym_to_check == ".":
            continue
        elif sym_to_check == "S":
            continue
        for sym_adjacency in PIPE_TYPES[sym_to_check]:
            print("  > Checking pos l {} + {} = {}, pos c {} + {} = {}".format(pos_l, sym_adjacency[0], check_position[0], pos_c, sym_adjacency[1], check_position[0]))
            if pos_l + sym_adjacency[0] == check_position[0] and pos_c + sym_adjacency[1] == check_position[1]:
                print("!!> Found adjacent at {}/{} = sum '{}'".format(pos_l, pos_c, sym_to_check))
                adjacent_positions.append((pos_l, pos_c))

    print("Adj ret: {}".format(adjacent_positions))
    return adjacent_positions


# add dots to make sure we don't go out of bound looking
values_input = ["." + x.strip() + "." for x in sys.stdin.readlines()]
values_input.insert(0, len(values_input[0]) * ".")
values_input.append(len(values_input[0]) * ".")

step_map = [["." for y in x] for x in values_input]

for line in values_input:
    print(line)

s_symbol_position = ()
starting_positions = []
for i, line in enumerate(values_input):
    try:
        s_symbol_position = (i, line.index("S"))
    except ValueError:
        pass

print("S symbol found at {}".format(s_symbol_position))

starting_positions = find_adjacent_pipes(values_input, s_symbol_position)
print("Found starting positions: {}\n".format(starting_positions))
previous_positions = [(-1, -1), (-1, -1)]

for i in itertools.count(start=2, step=1):
    for posi, position_to_check in enumerate(starting_positions):
        print("See prev {}".format(previous_positions[posi]))
        [(pos_l, pos_c)] = [x for x in find_adjacent_pipes(values_input, position_to_check) if x != previous_positions[posi]]
        step_map[pos_l][pos_c] = str(i)
        previous_positions[posi] = starting_positions[posi]
        print("Set prev {}".format(previous_positions[posi]))
        starting_positions[posi] = (pos_l, pos_c)

    # print("Step map:")
    # for line in step_map:
    #     print("".join(line))

    if starting_positions[0] == starting_positions[1]:
        print("Max distance acheived: {}".format(i))
        break
