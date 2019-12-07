import os
from itertools import permutations
import math

class IntcodeComputer:

  def __init__(self, program_input, phase_setting=None):
    self.program_input = program_input[:]
    self.inputs = []
    self.pointer = 0
    if phase_setting != None:
      self.inputs.append(phase_setting)

  def __read__(self, mode, param_no):
    if mode == '1':
      return self.pointer + param_no
    else:
      return self.program_input[self.pointer + param_no]

  def run_program(self, signal=None):
    instruction = str(self.program_input[self.pointer]).zfill(5)
    
    if signal != None:
      self.inputs.append(signal)

    while instruction[-2:] != '99':
      opcode, first_param_mode, second_param_mode, third_param_mode = instruction[-2:], instruction[2], instruction[1], instruction[0]
      if opcode in ('03', '04'):
        first_param = self.__read__(first_param_mode, 1)
      if opcode in ('05', '06'):
        first_param = self.__read__(first_param_mode, 1)
        second_param = self.__read__(second_param_mode, 2)
      if opcode in ('01', '02', '07', '08'):
        first_param = self.__read__(first_param_mode, 1)
        second_param = self.__read__(second_param_mode, 2)
        third_param = self.__read__(third_param_mode, 3)

      if opcode == '01':
        self.program_input[third_param] = self.program_input[first_param] + self.program_input[second_param]
        self.pointer += 4
      elif opcode == '02':
        self.program_input[third_param] = self.program_input[first_param] * self.program_input[second_param]
        self.pointer += 4
      elif opcode == '03':
        self.program_input[first_param] = self.inputs.pop(0)
        self.pointer += 2
      elif opcode == '04':
        self.pointer += 2
        return self.program_input[first_param]
      elif opcode == '05':
        if self.program_input[first_param] != 0:
          self.pointer = self.program_input[second_param]
        else:
          self.pointer += 3
      elif opcode == '06':
        if self.program_input[first_param] == 0:
          self.pointer = self.program_input[second_param]
        else:
          self.pointer += 3
      elif opcode == '07':
        if self.program_input[first_param] < self.program_input[second_param]:
          self.program_input[third_param] = 1
        else:
          self.program_input[third_param] = 0
        self.pointer += 4
      elif opcode == '08':
        if self.program_input[first_param] == self.program_input[second_param]:
          self.program_input[third_param] = 1
        else:
          self.program_input[third_param] = 0
        self.pointer += 4
      else:
        raise Exception(f'{instruction}, {opcode}')

      instruction = str(self.program_input[self.pointer]).zfill(5)

if __name__ == '__main__':
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', 'r') as reader:
        puzzle_input = [int(value) for value in reader.read().split(',')]

    part1 = -math.inf
    for phase_setting_config in permutations(range(5)):
      amplifiers = [IntcodeComputer(puzzle_input, phase_setting) for phase_setting in phase_setting_config]
      
      previous_amplifier_output = 0
      for amplifier in amplifiers:
        previous_amplifier_output = amplifier.run_program(previous_amplifier_output)
      part1 = max(previous_amplifier_output, part1)
    print(part1)

    part2 = -math.inf
    for phase_setting_config in permutations(range(5, 10)):
      amplifiers = [IntcodeComputer(puzzle_input, phase_setting) for phase_setting in phase_setting_config]

      previous_amplifier_output = 0
      while True:
        for amplifier in amplifiers:
          previous_amplifier_output = amplifier.run_program(previous_amplifier_output)

        if previous_amplifier_output:
          part2 = max(previous_amplifier_output, part2)
        else:
          break
    print(part2)