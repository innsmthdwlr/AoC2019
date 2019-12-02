import math
import os

with open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', 'r') as reader:
    mass = [int(x) for x in reader.read().splitlines()]

def calculate_fuel(mass):
  fuel_required = math.floor(mass / 3) - 2
  if fuel_required <= 0:
    return 0
  else:
    return fuel_required + calculate_fuel(fuel_required)

if __name__ == '__main__':
    fuel_req = sum([math.floor(x / 3) - 2 for x in mass])
    total_fuel_req = sum([calculate_fuel(x) for x in mass])

    print(fuel_req)
    print(total_fuel_req)