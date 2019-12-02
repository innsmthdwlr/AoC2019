puzzle_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,13,23,1,23,10,27,1,13,27,31,2,31,10,35,1,35,9,39,1,39,13,43,1,13,43,47,1,47,13,51,1,13,51,55,1,5,55,59,2,10,59,63,1,9,63,67,1,6,67,71,2,71,13,75,2,75,13,79,1,79,9,83,2,83,10,87,1,9,87,91,1,6,91,95,1,95,10,99,1,99,13,103,1,13,103,107,2,13,107,111,1,111,9,115,2,115,10,119,1,119,5,123,1,123,2,127,1,127,5,0,99,2,14,0,0]

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

print(run_program(reset_values(puzzle_input,12,2)))
print(part2(puzzle_input, 19690720))