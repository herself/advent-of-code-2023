#!/usr/bin/python3

import sys
import re
from collections import defaultdict

gear_ratios_sum = 0
star_catcher = re.compile("(\*)")
number_catcher = re.compile("(\d+)")

number_matches_by_line = defaultdict(list)
star_match_list = []
input_line_list = []

for lineno, line in enumerate(sys.stdin):
    input_line_list.append(line.strip())
    print(line.strip())
    for star_match in star_catcher.finditer(line.strip()):
        star_match_list.append((lineno, star_match))
    for number_match in number_catcher.finditer(line.strip()):
        number_matches_by_line[lineno].append(number_match)

for lineno, star_match in star_match_list:
    print("\n", lineno, star_match)
    surround_start = star_match.start() - 1 if star_match.start() > 1 else 0
    surround_end = star_match.end() + 1

    gear_ratio = 0
    surrounding_number_matches = []
    full_surrounding_numbers = []
    if lineno != 0:
        line_above = input_line_list[lineno - 1 if lineno > 1 else 0][surround_start:surround_end]
        print(" > {}".format(line_above))
        for surrounding_match in number_catcher.finditer(line_above):
            surrounding_number_matches.append((-1, surrounding_match))

    line_with_star = input_line_list[lineno][surround_start:surround_end]
    print(" > {}".format(line_with_star))
    for surrounding_match in number_catcher.finditer(line_with_star):
        surrounding_number_matches.append((0, surrounding_match))

    if lineno != len(input_line_list) - 1:
        line_below = input_line_list[lineno + 1][surround_start:surround_end]
        print(" > {}".format(line_below))
        for surrounding_match in number_catcher.finditer(line_below):
            surrounding_number_matches.append((1, surrounding_match))

    print(" >> {}".format(surrounding_number_matches))
    if len(surrounding_number_matches) == 2:
        print(" >> gear found at position: {}".format(star_match.start()))
        print(" >> possible num start ends: {}-{}".format(star_match.start()-1, star_match.end()))
        for pos, number_match in surrounding_number_matches:
            print(" >>> stuff to analyze: {}".format(number_matches_by_line[lineno+pos]))
            for possible_number_match in number_matches_by_line[lineno+pos]:
                #number ends near gear
                #print(" >>>> end {} <= {}, {} >= {}".format(possible_number_match.end(), star_match.end(), possible_number_match.end(), star_match.start()))
                #print(" >>>> start {} >= {}, {} <= {}".format(possible_number_match.start(), star_match.start(), possible_number_match.start(), star_match.end()))
                if possible_number_match.end() <= star_match.end() and possible_number_match.end() >= star_match.start():
                    print(" >>>> number ends near gear: {}".format(possible_number_match.group(0)))
                    full_surrounding_numbers.append(possible_number_match.group(0))
                #number starts near gear
                elif possible_number_match.start() >= star_match.start()-1 and possible_number_match.start() <= star_match.end():
                    print(" >>>> number starts near gear: {}".format(possible_number_match.group(0)))
                    full_surrounding_numbers.append(possible_number_match.group(0))
                #number goes through gear
                elif star_match.start() > possible_number_match.start() and star_match.end() < possible_number_match.end():
                    print(" >>>> number goes through gear: {}".format(possible_number_match.group(0)))
                    full_surrounding_numbers.append(possible_number_match.group(0))
        #ugly ugly deduplicating hax, still better than rewriting half the code above
        full_surrounding_numbers = list(set(full_surrounding_numbers))
        print(" >> numbers found near gear: {}".format(full_surrounding_numbers))
        assert(len(full_surrounding_numbers) == 2)

        gear_ratio = int(full_surrounding_numbers[0]) * int(full_surrounding_numbers[1])
        print(" >> gear ratio: {}".format(gear_ratio))
        gear_ratios_sum += gear_ratio

print("Gear ratio sum: {}".format(gear_ratios_sum))
