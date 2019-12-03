import os
from shapely.geometry import LineString, Point

def draw(circuit):
    current_location = (0, 0)
    points = [(0, 0)]
    for direction, distance in circuit:
        if direction == 'r':
            current_location = (current_location[0] + distance, current_location[1])
        elif direction == 'l':
            current_location = (current_location[0] - distance, current_location[1])
        elif direction == 'u':
            current_location = (current_location[0], current_location[1] + distance)
        elif direction == 'd':
            current_location = (current_location[0], current_location[1] - distance)
        points.append(current_location)
    return points

def get_crossings(circuitA, circuitB):
    crossings = []
    linesA = LineString(circuitA)
    linesB = LineString(circuitB)

    crossing_points = linesA.intersection(linesB)
    for crossing_point in crossing_points:
        if not crossing_point.is_empty and crossing_point.coords[:][0] not in crossings and crossing_point.coords[:][0] != (0, 0):
            crossings.append(crossing_point.coords[:][0])
       
    return crossings

def calculate_manhattan(point, origin = (0,0)):
    result = abs(point[0] - origin[0]) + abs(point[1] - origin[1])
    return result

def traverse_to(circuit, destination_coords):
    step = 0
    previous_point = (0, 0)
    lines = []
    destination = Point(destination_coords)
    for point in circuit[1:]:
        line = LineString([previous_point, point])
        if line.contains(destination):
            step += calculate_manhattan(destination_coords, previous_point)
            break
        step += calculate_manhattan(point, previous_point)
        previous_point = point
    return step


if __name__ == '__main__':
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', 'r') as reader:
        puzzle_input = [value for value in reader.read().splitlines()]
    wireA = [[item[0:1].lower(), int(item[1:])] for item in puzzle_input[0].split(',')]
    wireB = [[item[0:1].lower(), int(item[1:])] for item in puzzle_input[1].split(',')]

    circuitA = draw(wireA)
    circuitB = draw(wireB)

    crossings = get_crossings(circuitA, circuitB)
    closest_crossing = min(crossings, key=calculate_manhattan)
    fastest_crossing = min([traverse_to(circuitA, destination) + traverse_to(circuitB, destination) for destination in crossings])
    
    part1 = calculate_manhattan(closest_crossing)
    part2 = fastest_crossing

    print(part1)
    print(part2)


