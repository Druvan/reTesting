import unittest
import re

value = "aaaaa"

value_caps = "aaaaa AAAAA"


class subnTest(unittest.TestCase):
    def test_subn(self):

        self.assertEqual(re.subn("a", "b", value), ("bbbbb", 5))
        self.assertEqual(re.subn("a", "b", value_caps), ("bbbbb AAAAA", 5))
        self.assertEqual(re.subn("a", "b", value, 3, 1), ("bbbaa", 3))
        self.assertEqual(re.subn("a", "b", "ccccc"), ("ccccc", 0))
        self.assertEqual(re.subn("", "", "",), ("", 1))
        self.assertEqual(re.subn("@", "€€€", "@%@"), ("€€€%€€€", 2))
        self.assertRaises(TypeError, re.subn, "a", 1)


if __name__ == '__main__':
    unittest.main()