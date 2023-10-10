# Can you translate this driver code to unit tests?

import unittest
from char_count import char_count

class TestCharCount(unittest.TestCase):

    def test_char_count_example_1(self):
        result = char_count("aaabbc")
        expected = [
            ["a", 3],
            ["b", 2],
            ["c", 1]
        ]
        self.assertEqual(result, expected)

    def test_char_count_example_2(self):
        result = char_count("an apple a day will keep the doctor away")
        expected = [
            ["a", 6],
            ["e", 4],
            ["l", 3],
            ["p", 3],
            ["d", 2],
            ["o", 2],
            ["t", 2],
            ["w", 2],
            ["y", 2],
            ["c", 1],
            ["h", 1],
            ["i", 1],
            ["k", 1],
            ["n", 1],
            ["r", 1]
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
