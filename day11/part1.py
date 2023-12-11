#!/usr/bin/python3

import sys
import itertools

values_input = [x.strip() for x in sys.stdin.readlines()]


def calc_point_distance(point_a, point_b):
    (line_a, col_a) = point_a
    (line_b, col_b) = point_b
    return (max(line_a, line_b) - min(line_a, line_b)) + (max(col_a, col_b) - min(col_a, col_b))


# expand empty lines
values_exp_lines = []
for line in values_input:
    values_exp_lines.append(line)
    if all(y == "." for y in line):
        values_exp_lines.append(line)

# expand empty cols
values_exp_cols = [[] for line in values_exp_lines]
for col in range(len(values_exp_lines[0])):
    empty_col = True
    for line in range(len(values_exp_lines)):
        symbol_proc = values_exp_lines[line][col]
        if symbol_proc != ".":
            empty_col = False
        values_exp_cols[line].append(symbol_proc)
    if empty_col:
        for line in range(len(values_exp_lines)):
            values_exp_cols[line].append(".")

galaxy_coords = []
for line in range(len(values_exp_cols)):
    for col in range(len(values_exp_cols[0])):
        if values_exp_cols[line][col] == "#":
            galaxy_coords.append((line, col))

print(sum([calc_point_distance(point_a, point_b) for point_a, point_b in itertools.combinations(galaxy_coords, 2)]))
