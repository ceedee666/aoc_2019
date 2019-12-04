import pytest
import day_04

def test_increasing_digits():
    assert day_04.increasing_digits(1123445) == True
    assert day_04.increasing_digits(1121445) == False

def test_check_same_digit():
    assert day_04.check_same_digit(("1", False), "1") == ("1", True)
    assert day_04.check_same_digit(("1", False), "2") == ("2", False)
    assert day_04.check_same_digit(("1", True) , "2") == ("2", True)

def test_at_least_two_adjacent_digits():
    assert day_04.at_least_two_adjacent_digits(123456) == False
    assert day_04.at_least_two_adjacent_digits(111111) == True
    assert day_04.at_least_two_adjacent_digits(121212) == False
    assert day_04.at_least_two_adjacent_digits(123455) == True

def test_exactly_two_adjacent_digits():
    assert day_04.exactly_two_adjacent_digits(111122) == True
    assert day_04.exactly_two_adjacent_digits(123444) == False
    assert day_04.exactly_two_adjacent_digits(112233) == True

def test_password_candidates():
    assert day_04.password_candidates_part_1(range(111111, 111112)) == [111111]
    assert day_04.password_candidates_part_1(range(223450, 223451)) == []
    assert day_04.password_candidates_part_1(range(123789, 123790)) == []