#!/usr/bin/python3

import sys
import re

parts_number_sum = 0

number_catcher = re.compile("(\d+)")
symbol_catcher = re.compile("([^.0-9])")
number_match_list = []
input_line_list = []

for lineno, line in enumerate(sys.stdin):
    input_line_list.append(line.strip())
    print(line.strip())
    for number_match in number_catcher.finditer(line.strip()):
        number_match_list.append((lineno, number_match))

print()

for lineno, number_match in number_match_list:
    print(lineno, number_match)
    surround_start = number_match.start() - 1 if number_match.start() > 1 else 0
    surround_end = number_match.end() + 1

    line_with_surroudings_contents = str()
    if lineno != 0:
        line_above = input_line_list[lineno - 1 if lineno > 1 else 0][surround_start:surround_end]
        print(" > {}".format(line_above))
        line_with_surroudings_contents += line_above

    line_with_number = input_line_list[lineno][surround_start:surround_end]
    print(" > {}".format(line_with_number))
    line_with_surroudings_contents += line_with_number

    if lineno != len(input_line_list) - 1:
        line_below = input_line_list[lineno + 1][surround_start:surround_end]
        print(" > {}".format(line_below))
        line_with_surroudings_contents += line_below

    print(" >> {}".format(line_with_surroudings_contents))
    if symbol_catcher.search(line_with_surroudings_contents):
        print(" >> {}".format(number_match.group(1)))
        parts_number_sum += int(number_match.group(1))

print("Sum of all the parts: {}".format(parts_number_sum))
