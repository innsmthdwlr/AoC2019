import os
from itertools import permutations
import math

class IntcodeComputer:

  def __init__(self, program_input, phase_setting=None):
    self.program_input = program_input[:]
    self.pointer = 0
    self.relative_base = 0
    self.memory = []
    if phase_setting != None:
      self.memory.append(phase_setting)
  
  def __write__(self, param_no, value, mode='1'):
    if mode == '0': #position mode
      self.program_input[self.program_input[self.pointer + param_no]] = value
    elif mode == '1': #immediate mode
      self.program_input[self.pointer + param_no] = value
    else: #relative mode
      self.program_input[self.relative_base + self.program_input[self.pointer + param_no]] = value

  def __read__(self, mode, param_no):
    if mode == '0': #position mode
      return self.program_input[self.pointer + param_no]
    elif mode == '1': #immediate mode
      return self.pointer + param_no
    else: #relative mode
      return self.relative_base + self.program_input[self.pointer + param_no]

  def run_program(self, signal=None):
    
    if signal != None:
      self.memory.append(signal)
    instruction = str(self.program_input[self.pointer]).zfill(5)

    while instruction[-2:] != '99':
      opcode, first_param_mode, second_param_mode, third_param_mode = instruction[-2:], instruction[2], instruction[1], instruction[0]
      if opcode in ('03', '04', '09'):
        first_param = self.__read__(first_param_mode, 1)
      if opcode in ('05', '06'):
        first_param = self.__read__(first_param_mode, 1)
        second_param = self.__read__(second_param_mode, 2)
      if opcode in ('01', '02', '07', '08'):
        first_param = self.__read__(first_param_mode, 1)
        second_param = self.__read__(second_param_mode, 2)
        third_param = self.__read__(third_param_mode, 3)

      if opcode == '01':
        value = self.program_input[first_param] + self.program_input[second_param]
        self.__write__(3, value, third_param_mode)
        self.pointer += 4
      elif opcode == '02':
        value = self.program_input[first_param] * self.program_input[second_param]
        self.__write__(3, value, third_param_mode)
        self.pointer += 4
      elif opcode == '03':
        print(f"input signal: {self.memory}")
        value = self.memory.pop(0)
        self.__write__(1, value, first_param_mode)
        self.pointer += 2
      elif opcode == '04':
        value = self.program_input[first_param]
        print(f"coordinates: {value}")
        self.memory.append(value)
        self.pointer += 2
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
          self.__write__(3, 1, third_param_mode)
        else:
          self.__write__(3, 0, third_param_mode)
        self.pointer += 4
      elif opcode == '08':
        if self.program_input[first_param] == self.program_input[second_param]:
          self.__write__(3, 1, third_param_mode)
        else:
          self.__write__(3, 0, third_param_mode)
        self.pointer += 4
      elif opcode == '09':
        self.relative_base += self.program_input[first_param]
        self.pointer += 2
      else:
        print(f'Unknown opcode in {instruction} at [{self.pointer}]')
        break

      instruction = str(self.program_input[self.pointer]).zfill(5)

if __name__ == '__main__':
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', 'r') as reader:
        puzzle_input = [int(value) for value in reader.read().split(',')]
    puzzle_input.extend([0]*10000)
    
    computer = IntcodeComputer(puzzle_input)
    part1 = computer.run_program(1)
    
    computer = IntcodeComputer(puzzle_input)
    part2 = computer.run_program(2)