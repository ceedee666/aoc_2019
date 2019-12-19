import pytest
from day_18 import *

def test_find_start_positions():
    maze = [ \
        "#########", \
        "#b.A.@.a#", \
        "#########"]

    assert find_start_positions(maze) == [(1,5)]