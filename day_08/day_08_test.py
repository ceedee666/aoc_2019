import pytest
import day_08

def test_split_list():
    assert day_08.split_list([1,2,3,4,5,6,7,8,9],3) == [[1,2,3], [4,5,6], [7,8,9]]

def test_convert_input_to_layers():
    assert day_08.convert_input_to_layers([1,2,3,4,5,6,7,8,9,0,1,2], 3, 2) == [[1,2,3,4,5,6],[7,8,9,0,1,2]]

def test_count_colors_in_layer():
    layer = [1,2,3,1,1,2,1,1,1]
    colors_count = day_08.count_colors_in_layer(layer)
    assert colors_count[1] == 6
    assert colors_count[2] == 2
    assert colors_count[3] == 1

def test_count_colors_in_layers():
    layers = [[1,1,1,1,1],[2,2,3,3,3]]
    colors_count = day_08.count_colors_in_layers(layers)
    assert colors_count[0][1] == 5
    assert colors_count[0][2] == 0
    assert colors_count[0][3] == 0

    assert colors_count[1][1] == 0
    assert colors_count[1][2] == 2
    assert colors_count[1][3] == 3

def test_layer_with_minimal_0():
    layers = [[0,0,1,1,1,1,2,2],[0,2,1,1,1,1,2,2],[0,0,1,1,0,1,2,2]]
    layer = day_08.layer_with_minimal_0(day_08.count_colors_in_layers(layers))
    assert layer[0] == 1
    assert layer[1] == 4
    assert layer[2] == 3

def test_decode_image():
    input = list(map(int, "0222112222120000"))
    result = day_08.decode_image(day_08.convert_input_to_layers(input,2,2))
    assert result == [0,1,1,0]