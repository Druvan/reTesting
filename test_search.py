import unittest
import re

value = "aabaa"


class SearchTest(unittest.TestCase):
    def test_search(self):

        self.assertEqual(re.search("b", value).span(), (2, 3))
        self.assertEqual(re.search("a", value).span(), (0, 1))
        self.assertEqual(re.search("c", value), None)
        self.assertEqual(re.search("1", value), None)
        self.assertEqual(re.search("", "").span(), (0, 0))
        self.assertEqual(re.search("@", "%@").span(), (1, 2))
        self.assertRaises(TypeError, re.search, "a", 1)
        self.assertRaises(TypeError, re.search, "a", True)


if __name__ == '__main__':
    unittest.main()

