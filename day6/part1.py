#!/usr/bin/python3

import sys
from functools import reduce

race_total_times = [int(x) for x in sys.stdin.readline().split(":")[1].split()]
race_top_distances = [int(x) for x in sys.stdin.readline().split(":")[1].split()]
race_ways_record_beat = []

print("Got time list: {}".format(race_total_times))
print("Got distance list: {}".format(race_top_distances))

for i, (race_total_time, top_distance) in enumerate(zip(race_total_times, race_top_distances)):
    print("Calculating race with time={} and distance={}".format(race_total_time, top_distance))
    race_ways_record_beat.append(0)
    for this_time_pressed in range(1, race_total_time):
        distance_travelled = this_time_pressed * (race_total_time - this_time_pressed)
        if(distance_travelled > top_distance):
            race_ways_record_beat[i] += 1

ways_to_win_multiplied = reduce(lambda x, y: x * y, race_ways_record_beat)
print(ways_to_win_multiplied)
