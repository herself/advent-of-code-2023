#!/usr/bin/python3

import sys

race_total_time = int(sys.stdin.readline().split(":")[1].replace(" ", ""))
top_distance = int(sys.stdin.readline().split(":")[1].replace(" ", ""))

print("Got time list: {}".format(race_total_time))
print("Got distance list: {}".format(top_distance))

first_winning_time = 0
print("Calculating race with time={} and distance={}".format(race_total_time, top_distance))
for this_time_pressed in range(1, race_total_time):
    distance_travelled = this_time_pressed * (race_total_time - this_time_pressed)
    if(distance_travelled > top_distance):
        first_winning_time = this_time_pressed
        break
ways_to_win = race_total_time - (2 * first_winning_time) + 1
print(ways_to_win)
