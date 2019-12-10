import os
from math import gcd, atan2

def raycast(station, asteroid_field):
    hits = set()
    
    for asteroid in asteroid_field:
        if asteroid != station:
                dv, dh = asteroid[0] - station[0], asteroid[1] - station[1]
                g = abs(gcd(dv, dh))
                red = (dv // g, dh // g)
                hits.add(red)
    return hits

def get_asteroid_field(puzzle_input):
    height, width = len(puzzle_input), len(puzzle_input[0])
    asteroid_field = set()

    for v in range(height):
        for h in range(width):
            if puzzle_input[v][h] == "#":
                    asteroid_field.add((v, h))    
    return asteroid_field

if __name__ == '__main__':
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', 'r') as reader:
        puzzle_input = reader.read().splitlines()
    asteroid_field = get_asteroid_field(puzzle_input)
    
    station_candidates = []
    for candidate in asteroid_field:
        in_sight = raycast(candidate, asteroid_field)
        station_candidates.append((len(in_sight), candidate, in_sight))
    station_candidates.sort(reverse = True)
    part1, station_coordinates, in_sight = station_candidates[0]
    print(part1)

    destroyed = [ (atan2(dh, dv), (dv, dh)) for dv, dh in in_sight]
    destroyed.sort(reverse = True)
    dv, dh = destroyed[200-1][1]
    v, h = station_coordinates[0] + dv, station_coordinates[1] + dh
    while (v, h) not in asteroid_field:
        v, h = v + dv, h + dh

    part2 = h * 100 + v
    print(part2)