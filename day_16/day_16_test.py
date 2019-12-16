import pytest
from day_16 import *

def test_build_repeating_pattern():
    test_pattern = [0, 1, 1, 0, 0, -1, -1, 0, 0, 1, 1, 0, 0, -1, -1]
    assert build_repeating_pattern(1, len(test_pattern)) == test_pattern

def test_correction_step():
    transmission = list(map(int, list("12345678")))
    result = list(map(int, list("48226158")))
    assert correction_step(transmission) == result

    transmission = result
    result = list(map(int, list("34040438")))
    assert correction_step(transmission) == result

    transmission = result
    result = list(map(int, list("03415518")))
    assert correction_step(transmission) == result

    transmission = result
    result = list(map(int, list("01029498")))
    assert correction_step(transmission) == result

def test_correct_transmission_with_FFT():
    transmission = list(map(int, list("80871224585914546619083218645595")))
    result = list(map(int, list("24176176")))
    assert correct_transmission_with_FFT(transmission)[:8] == result


