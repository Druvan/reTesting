import unittest
import re

value = "aabaa"


class MatchTest(unittest.TestCase):
    def test_match(self):

        self.assertEqual(re.match("a", "a").span(), (0, 1))
        self.assertEqual(re.match("b", value), None)
        self.assertEqual(re.match("a", value).span(), (0, 1))
        self.assertEqual(re.match("c", value), None)
        self.assertEqual(re.match("1", value), None)
        self.assertEqual(re.match("", "").span(), (0, 0))
        self.assertEqual(re.match("a", ""), None)
        self.assertEqual(re.match("@", "@%").span(), (0, 1))
        self.assertRaises(TypeError, re.match, "a", 1)
        self.assertRaises(TypeError, re.match, "a", True)


if __name__ == '__main__':
    unittest.main()

