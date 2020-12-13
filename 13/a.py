#!/usr/bin/env python3

"""Calculate earliest departure for every bus, take overall earliest one."""


import fileinput


def sol(lines):
    arrival_time = int(lines[0])
    bus_durations = list(map(int, [n for n in lines[1].split(',') if n != 'x']))

    earliest_departure = float('inf')
    earliest_duration = None
    for duration in bus_durations:
        next_departure = (arrival_time // duration) * duration
        if next_departure < arrival_time:
            next_departure += duration  # previous one was in the past
        if next_departure < earliest_departure:
            earliest_departure, earliest_duration = next_departure, duration

    print((earliest_departure - arrival_time) * earliest_duration)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
