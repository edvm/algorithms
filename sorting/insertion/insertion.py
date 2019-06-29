import random

def sort(numbers):
    """Sort a list of numbers using `insertion sort` algorithm."""
    return numbers


if __name__ == '__main__':
    numbers = [ random.randint(0, 100) for x in range(0, 100) ]
    _sorted = sort(numbers)
    assert _sorted == sorted(numbers), f"Its not sorted :(\n{_sorted}"