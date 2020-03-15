import time
import string
import random

letters = string.ascii_lowercase + " "
sheakespeare_phrase = "methinks it is like a weasel"


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


def get_random_text(length: int) -> str:
    """Returns a text of given length."""
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
    t1 = time.time()
    best_phrase, best_score, n_iterations = generate(phrase, repeat)
    t2 = time.time()

    print(f"Best match: {best_phrase}")
    print(f"Iterations: {repeat - n_iterations}")
    print(f"Score: {best_score}")
    print("Time elapsed: %.3f seconds" % (t2 - t1))
