import unittest
import monkey


class TestMonkey(unittest.TestCase):
    def test_get_random_text(self):
        text = monkey.get_random_text(10)
        self.assertTrue(isinstance(text, str))
        self.assertEqual(len(text), 10)

        text = monkey.get_random_text(0)
        self.assertEqual(text, "")
        self.assertEqual(len(text), 0)

    def test_get_index_positions_of(self):
        array = [1, 0, 0, 1]
        self.assertEqual([1, 2], monkey.get_index_positions_of(0, array))
        self.assertEqual([0, 3], monkey.get_index_positions_of(1, array))
        array = [-1, 0, 0, -1]
        self.assertEqual([0, 3], monkey.get_index_positions_of(-1, array))
        array = [-1, -1, -1, -1]
        self.assertEqual([0, 1, 2, 3], monkey.get_index_positions_of(-1, array))
        array = [0, 0, 0, 0]
        self.assertEqual([], monkey.get_index_positions_of(-1, array))
        array = []
        self.assertEqual([], monkey.get_index_positions_of(1, array))
        self.assertEqual([], monkey.get_index_positions_of(0, array))
        self.assertEqual([], monkey.get_index_positions_of(-1, array))

    def test_get_index_positions_to_guess(self):
        self.assertEqual([3], monkey.get_index_positions_to_guess("qwee", "qwer"))
        self.assertEqual([0, 3], monkey.get_index_positions_to_guess(" wee", "qwer"))
        self.assertEqual([0, 2, 3], monkey.get_index_positions_to_guess(" w3e", "qwer"))
        self.assertEqual([], monkey.get_index_positions_to_guess("", ""))


if __name__ == "__main__":
    unittest.main()
