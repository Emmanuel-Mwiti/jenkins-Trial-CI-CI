# TestOperations.py
from AddNumbers import add_numbers
from SubtractNumbers import subtract_numbers

def test_addition():
    result = add_numbers(5, 3)
    assert result == 8, "Test case 1 (addition) failed"

    result = add_numbers(-2, -7)
    assert result == -9, "Test case 2 (addition) failed"

    result = add_numbers(10, -4)
    assert result == 6, "Test case 3 (addition) failed"

    result = add_numbers(3.5, 1.5)
    assert result == 5.0, "Test case 4 (addition) failed"

def test_subtraction():
    result = subtract_numbers(5, 3)
    assert result == 2, "Test case 1 (subtraction) failed"

    result = subtract_numbers(-2, -7)
    assert result == 5, "Test case 2 (subtraction) failed"

    result = subtract_numbers(10, -4)
    assert result == 14, "Test case 3 (subtraction) failed"

    result = subtract_numbers(3.5, 1.5)
    assert result == 2.0, "Test case 4 (subtraction) failed"

if __name__ == "__main__":
    test_addition()
    test_subtraction()
    print("All tests passed.")
