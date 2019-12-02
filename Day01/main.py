import math
import os
from functools import reduce

with open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', 'r') as reader:
    mass = [int(value) for value in reader.read().splitlines()]

def calculate_fuel(mass):
    return math.floor(mass / 3) - 2

def calculate_fuel_total(mass):
  fuel_required = calculate_fuel(mass)
  if fuel_required <= 0:
    return 0
  else:
    return fuel_required + calculate_fuel_total(fuel_required)

if __name__ == '__main__':
    print(sum([calculate_fuel(x) for x in mass]))
    print(sum([calculate_fuel_total(x) for x in mass]))