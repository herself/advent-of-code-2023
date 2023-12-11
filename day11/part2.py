#!/usr/bin/python3

import sys
import itertools

EXPANDED_GALAXY_SIZE = 1000000
values_input = [x.strip() for x in sys.stdin.readlines()]


def calc_point_distance(point_a, point_b):
    (line_a, col_a) = point_a
    (line_b, col_b) = point_b
    expanded_distance = 0
    for expanded_lineno in empty_lines_list:
        if max(line_a, line_b) > expanded_lineno > min(line_a, line_b):
            expanded_distance += EXPANDED_GALAXY_SIZE - 1
    for expanded_colno in empty_cols_list:
        if max(col_a, col_b) > expanded_colno > min(col_a, col_b):
            expanded_distance += EXPANDED_GALAXY_SIZE - 1
    return (max(line_a, line_b) - min(line_a, line_b)) + (max(col_a, col_b) - min(col_a, col_b)) + expanded_distance


empty_lines_list = []
for lineno, line in enumerate(values_input):
    if all(y == "." for y in line):
        empty_lines_list.append(lineno)

empty_cols_list = []
for col in range(len(values_input[0])):
    empty_col = True
    for line in range(len(values_input)):
        if values_input[line][col] != ".":
            empty_col = False
    if empty_col:
        empty_cols_list.append(col)

print("Empty lines: {}".format(empty_lines_list))
print("Empty cols: {}".format(empty_cols_list))

galaxy_coords = []
for line in range(len(values_input)):
    for col in range(len(values_input[0])):
        if values_input[line][col] == "#":
            galaxy_coords.append((line, col))

print(sum([calc_point_distance(point_a, point_b) for point_a, point_b in itertools.combinations(galaxy_coords, 2)]))
