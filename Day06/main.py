import os
import networkx as nx

if __name__ == '__main__':
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', 'r') as reader:
        puzzle_input = [(x[0:3], x[4:]) if x[3] == '()' else (x[4:], x[0:3]) for x in [coord for coord in reader.read().splitlines()]]

    orbit_map = nx.DiGraph(puzzle_input)
    part1 = sum(len(nx.ancestors(orbit_map, n)) for n in orbit_map.nodes)
    
    starchart = nx.Graph(puzzle_input)
    origin = "YOU"
    destination = "SAN"
    part2 = len(nx.shortest_path(starchart, origin, destination)) - 3

    print(part1)
    print(part2)