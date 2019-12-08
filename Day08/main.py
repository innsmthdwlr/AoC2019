import os
import numpy as np

if __name__ == '__main__':
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', 'r') as reader:
        puzzle_input = [int(value) for value in reader.read()]
    width, height = 25, 6
    layers = np.array(puzzle_input)
    layers = layers.reshape(-1, height, width)
    
    zeros_on_layers = [(idx, np.sum(layer == 0)) for idx, layer in enumerate(layers)]
    layer_with_fewest_zeros = layers[min(zeros_on_layers, key=lambda val: val[1])[0]]
    part1 = np.sum(layer_with_fewest_zeros == 1) * np.sum(layer_with_fewest_zeros == 2)

    image = layers[0]
    for layer in layers:
        image = np.where(image != 2, image, layer)

    image = np.where(image == 1, '|', ' ')
    part2 = '\n'.join([''.join(row) for row in image])

    print(part1)
    print(part2)
