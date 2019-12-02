import os
    
def reset_values(program_input, noun, verb):
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
    result = 0

    if opcode == 1:
      result = program_input[pos_a] + program_input[pos_b]
    elif opcode == 2:
      result = program_input[pos_a] * program_input[pos_b]

    program_input[pos_result] = result
    next_opcode += 4
    opcode = program_input[next_opcode]
  return program_input[0]

def part2(program_input, required_output):
  max_pos = len(program_input)-1
  for noun in range(0, max_pos):
    for verb in range(0, max_pos):
      comm = reset_values(program_input, noun, verb)
      result = run_program(comm)
      if result == required_output:
        return 100 * comm[1] + comm[2]


if __name__ == '__main__':
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', 'r') as reader:
        puzzle_input = [int(x) for x in reader.read().split(',')]

    print(run_program(reset_values(puzzle_input,12,2)))
    print(part2(puzzle_input, 19690720))