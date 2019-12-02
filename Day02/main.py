import os
    
def reset_input(program_input, noun, verb):
  reset = program_input[:]
  reset[1] = noun
  reset[2] = verb
  return reset

def run_program(program_input):
  next_opcode = 0
  opcode = program_input[next_opcode]

  while opcode != 99:
    pos_a = program_input[next_opcode+1]
    pos_b = program_input[next_opcode+2]
    pos_result = program_input[next_opcode+3]

    if opcode == 1:
      program_input[pos_result] = program_input[pos_a] + program_input[pos_b]
    elif opcode == 2:
      program_input[pos_result] = program_input[pos_a] * program_input[pos_b]

    next_opcode += 4
    opcode = program_input[next_opcode]
  return program_input[0]

def find_noun_and_verb(program_input, required_output):
  max_pos = len(program_input)-1
  for noun in range(0, max_pos):
    for verb in range(0, max_pos):
      command_list = reset_input(program_input, noun, verb)
      result = run_program(command_list)
      if result == required_output:
        return 100 * command_list[1] + command_list[2]


if __name__ == '__main__':
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', 'r') as reader:
        puzzle_input = [int(value) for value in reader.read().split(',')]

    print(run_program(reset_input(puzzle_input, 12, 2)))
    print(find_noun_and_verb(puzzle_input, 19690720))