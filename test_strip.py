import unittest
import string

str = "000AAAAA000"
str_1 = "AAAAA000"

class StripTest(unittest.TestCase):

    def test_Strip(self):

        self.assertEqual(str.strip("0"), "AAAAA")
        self.assertEqual(str.strip("1"), "000AAAAA000")
        self.assertEqual(str.strip("@"), "000AAAAA000")
        self.assertEqual(str_1.strip("0"), "AAAAA")
        self.assertEqual(str.strip(""), "000AAAAA000")
        self.assertRaises(TypeError, str.strip, "a", 1)
        self.assertRaises(TypeError, str.strip, "a", True)


if __name__ == '__main__':
    unittest.main()




