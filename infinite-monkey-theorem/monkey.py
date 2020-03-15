import time
import string
import random

letters = string.ascii_lowercase + " "


def get_random_char(letters: str) -> str:
    """Returns a single random char from given letters."""
    return letters[random.randint(0, len(letters) - 1)]


def get_similarity_vector(string1: str, string2: str) -> list:
    """Returns a list like: [1, 0, 1].

    1 means char at that position on both strings are equal.
    2 means char at that position on both strings aren't equal.
    """
    assert len(string1) == len(string2), "All arguments must have the same length"

    vector = []
    for idx, ch in enumerate(string1):
        if string2[idx] == ch:
            vector.append(1)
        else:
            vector.append(0)

    return vector


def get_index_positions_of(n: int, iterable: list) -> list:
    positions = []
    to_iter = iterable.copy()
    n_toggled = -1 if n == 0 else n * -1
    while n in to_iter:
        position = to_iter.index(n)
        positions.append(position)
        to_iter[position] = n_toggled
    return positions


def get_index_positions_to_guess(string1: str, string2) -> list:
    """Returns a list of integer positions.

    Each element of the returned list meants that `string1` and `string2`
    are different at that given `element value`/position.

    For ex:

    >>> get_index_positions_to_guess("qwee", "qwer")
    [3]
    """
    vector = get_similarity_vector(string1, string2)
    positions = get_index_positions_of(0, vector)
    return positions


def get_random_text(length: int) -> str:
    text = ""
    while len(text) < length:
        text += get_random_char(letters)
    return text


def generate(phrase: str, repeat: int = 1000) -> tuple:
    """Returns a tuple like: ('random text', score, n_iterations) """
    best_phrase = ""
    best_score = 0

    while repeat > 0:
        repeat -= 1
        random_text = get_random_text(len(phrase))
        vector = get_similarity_vector(phrase, random_text)
        new_score = vector.count(1)
        if new_score > best_score:
            best_score = new_score
            best_phrase = random_text
        if best_score == len(phrase):
            break

    return (best_phrase, best_score, repeat)


def start_typing(phrase: str, repeat: int = 1000) -> tuple:
    """Tell your monkey to start typing!."""
    assert repeat > 0, "repeat argument cannot be zero"

    t1 = time.time()
    best_phrase, best_score, n_iterations = generate(phrase, repeat)
    t2 = time.time()
    total_iterations = repeat - n_iterations
    total_iterations_used_percent = 100 - (n_iterations * 100 / repeat)

    print(f"Best match: {best_phrase}")
    print(f"Iterations: {total_iterations}")
    print("Used %.2f percent of given iterations" % total_iterations_used_percent)
    print(f"Score: {best_score}")
    print("Time elapsed: %.3f seconds" % (t2 - t1))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
