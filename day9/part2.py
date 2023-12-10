#!/usr/bin/python3

import sys
from pprint import pprint


def calc_diff_list(input_list):
    current_list = [y - x for x, y in zip(input_list[0:], input_list[1:])]

    print("input: ", end="")
    pprint(input_list)
    print("current: ", end="")
    pprint(current_list)
    if all(x == 0 for x in current_list):
        return (0, current_list)
    else:
        (first, deeper_list) = calc_diff_list(current_list)
        return (current_list[0] - first, [current_list, deeper_list])


values_input = [[int(y) for y in x.strip().split()] for x in sys.stdin.readlines()]
pprint(values_input)

sum_extrapolated_values = 0
for values_set in values_input:
    diff, _ = calc_diff_list(values_set)
    sum_extrapolated_values += values_set[0] - diff

print("Extrapolated value sum: {}".format(sum_extrapolated_values))
