import random


def test_sort(mysort, expected, fname):
    """Util to test how i sorted."""
    assert len(mysort) == len(expected), "Dude, you are doing nasty things, correct your algo"
    assert mysort == expected, f"Its not sorted :(\n{mysort}\n{expected}"

    print(f'{fname} >>> Good job!')


def sort_1(numbers):
    """Sort a list of numbers using `insertion sort` algorithm."""

    for x, n1 in enumerate(numbers): 
        if x == 0:
            continue
        for j, n2 in enumerate(numbers[:x]):
            if n1 < n2:
                numbers[x], numbers[j] = n2, n1

    return numbers


if __name__ == '__main__':
    numbers = [ random.randint(0, 100) for x in range(0, 30) ]
    expected = sorted(numbers)
    test_sort(sort_1(numbers), expected, 'sort_1')