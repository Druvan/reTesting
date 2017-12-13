import stringProvider
import code
import unittest
import re
import textwrap
from textwrap_example import sample_text_longer


def splitter(string, sign):
    return string.split(sign)

def _upper(string):
    return string.upper()

def _lower(string):
    return string.lower()

def reg_fullmatch(pattern, text):

    if re.fullmatch(pattern, text):
        return True
    else:
        return False


def reg_full_match(pattern, text, flags):

    if re.fullmatch(pattern, text, flags):
        return True
    else:
        return False

def subber(toReplace, replaceWith, sourceStr):

    return re.sub(toReplace, replaceWith, sourceStr)

def wrap_fill(text):

    return textwrap.dedent(text).strip()



"""
    long string
    one character
    empty string
    non alphanumeric
    numbers
    built-in error types
    wrong data types


"""

class testStr(unittest.TestCase):

    def testSplit(self):

        self.assertEqual(splitter("a", ","), ['a'])
        self.assertEqual(splitter("", ","), [""])
        self.assertEqual(splitter("@,#,€", ","), ['@','#','€'])
        self.assertEqual(splitter("1,2,3", "k"), ["1,2,3"])
        self.assertRaises(TypeError, splitter, ("1,2", 3))
        self.assertRaises(TypeError, splitter, (1, 2, ','))
        self.assertRaises(ValueError, splitter, (""), (""))
        self.assertEqual(splitter("1,2,3", ","), ['1', '2', '3'])

    def testUpper(self):

        self.assertEqual(_upper("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
                                , "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
        self.assertEqual(_upper("å"), 'Å')
        self.assertEqual(_upper(""), "")
        self.assertEqual(_upper("%€#"), "%€#")
        self.assertRaises(AttributeError, _upper, (123))
        self.assertRaises(AttributeError, _upper, ({"bla" : 5}))

    def testFullMatch(self):

        self.assertEqual(reg_fullmatch("ökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehb", "ökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehb"), True)
        self.assertEqual(reg_fullmatch("x", "x"), True)
        self.assertEqual(reg_fullmatch("", ""), True)
        self.assertEqual(reg_fullmatch("1", ""), False)
        self.assertEqual(reg_fullmatch("", "1"), False)
        self.assertRaises(TypeError, reg_fullmatch, (1, ""))
        self.assertRaises(TypeError, reg_fullmatch, (True, True))
        self.assertRaises(TypeError, reg_fullmatch, ("___________", 198345093845))
        self.assertRaises(ValueError, reg_full_match, ("x"), ("x"), 4)
        self.assertEqual(reg_fullmatch("#%&/€=", "#%&/€="), True)
        self.assertEqual(reg_fullmatch("()?", "()?"), False)

    def testSub(self):
        self.assertEqual(subber("a", "b", stringProvider.testSubHelperA()), stringProvider.testSubHelperB())
        self.assertEqual(subber("a", "b", "a"), "b")
        self.assertEqual(subber("", "", ""), "")
        self.assertEqual(subber("@", "€€€", "@%@"), "€€€%€€€")
        self.assertRaises(TypeError, subber, 1, "b", "1234")
        self.assertRaises(TypeError, subber, "a", "b", {"kul":5})

    def testLower(self):
        self.assertEqual(_lower("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
                                , "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
        self.assertEqual(_lower("B"), 'b')
        self.assertEqual(_lower(""), "")
        self.assertEqual(_lower("%€#"), "%€#")
        self.assertRaises(AttributeError, _lower, (123))
        self.assertRaises(AttributeError, _lower, ({"bla" : 5}))

    def testWrap(self):
        self.assertEqual(wrap_fill(sample_text_longer),"paragraph\n  bbbbbbb\n    cccccc")
        self.assertEqual(wrap_fill("b"), "b")
        self.assertEqual(wrap_fill(""), "")
        self.assertEqual(wrap_fill("$$$\n   $$$\n  $$$"), "$$$\n   $$$\n  $$$")
        self.assertRaises(TypeError, wrap_fill, 123)

if __name__ == '__main__':
    unittest.main()
