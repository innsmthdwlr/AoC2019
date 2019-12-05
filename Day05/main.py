import os

def read(program_input, param, mode):
  if mode == '0':
    return program_input[param]
  else:
    return param

def get_params(program_input, pointer, first_param_mode, second_param_mode):
  first_param, second_param, write_to = 0, 0, 0

  try:
    first_param = read(program_input, program_input[pointer+1], first_param_mode)
    second_param = read(program_input, program_input[pointer+2], second_param_mode)
    write_to = program_input[pointer+3]  
  except IndexError:
    pass
  return first_param, second_param, write_to

def run_program(program_input, system_id):
  pointer = 0
  instruction = str(program_input[pointer]).zfill(5)
  buffer = system_id

  while instruction[-2:] != '99':
    opcode, first_param_mode, second_param_mode = instruction[-2:], instruction[2], instruction[1]
    first_param, second_param, write_to = get_params(program_input, pointer, first_param_mode, second_param_mode)

    if opcode == '01':
      program_input[write_to] = first_param + second_param
      pointer += 4
    elif opcode == '02':
      program_input[write_to] = first_param * second_param
      pointer += 4
    elif opcode == '03':
      program_input[write_to] = buffer
      pointer += 2
    elif opcode == '04':
      buffer = first_param
      pointer += 2
    elif opcode == '05':
      if first_param != 0:
        pointer = second_param
      else:
        pointer += 3
    elif opcode == '06':
      if first_param == 0:
        pointer = second_param
      else:
        pointer += 3
    elif opcode == '07':
      if first_param < second_param:
        program_input[write_to] = 1
      else:
        program_input[write_to] = 0
      pointer += 4
    elif opcode == '08':
      if first_param == second_param:
        program_input[write_to] = 1
      else:
        program_input[write_to] = 0
      pointer += 4
    else:
      raise Exception
    
    instruction = str(program_input[pointer]).zfill(5)
  return (program_input[0], buffer)

if __name__ == '__main__':
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', 'r') as reader:
        puzzle_input = [int(value) for value in reader.read().split(',')]
    part1_input = puzzle_input[:]
    part2_input = puzzle_input[:]

    print(run_program(part1_input, 1))
    print(run_program(part2_input, 5))