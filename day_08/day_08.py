from collections import defaultdict
from functools import reduce

def split_list(lst, n):
    return [list(lst[i:i+n]) for i in range(0, len(lst), n)]

def convert_input_to_layers(input, width, hight):
    return split_list(input, width * hight)

def count_colors_in_layer(layer):
    d = defaultdict(int)
    for pixel in layer:
        d[pixel] += 1
    return d

def count_colors_in_layers(layers):
    return [count_colors_in_layer(layer) for layer in layers]

def layer_with_minimal_0(colors_in_layers_list):
    min_0_layer = colors_in_layers_list[0]
    for colors_in_layer in colors_in_layers_list:
        if colors_in_layer[0] < min_0_layer[0]:
            min_0_layer = colors_in_layer
    return min_0_layer

def first_nontransparent_color(pixel, layers):
    for l in layers:
        if l[pixel] != 2:
            return l[pixel]

def decode_image(layers):
    result = []
    for pixel in range(len(layers[0])):
        result.append(first_nontransparent_color(pixel, layers))
    result = split_list(result,25)
    return result

if __name__ == "__main__":
    with open("day_08/input.txt") as f:
        input = list(map(int,f.read()))

    layer = layer_with_minimal_0(count_colors_in_layers(convert_input_to_layers(input, 25,6)))

    print("Number of 1s multiplied by number of 2s on layer with minimal 0s:", layer[1]*layer[2])
    print("The decoded message is:")

    for row in decode_image(convert_input_to_layers(input, 25,6)):
        print("".join("\u2588" if c == 1 else " " for c in row))