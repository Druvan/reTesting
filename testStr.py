import stringProvider
import code
import unittest
import re
import textwrap

def reg_fullmatch(pattern, text):

    if re.fullmatch(pattern, text):
        return True
    else:
        return False

class testStr(unittest.TestCase):

    def testSplit(self):

        self.assertEqual('a'.split(','), ['a'])
        self.assertEqual(''.split(','), [''])
        self.assertEqual("@,#,€".split(','),  ['@','#','€'])
        self.assertEqual('1,2,3'.split('k'), ['1,2,3'])
        self.assertRaises(TypeError, '1,2'.split, 3)
        self.assertRaises(ValueError, ''.split, '')
        self.assertEqual('1,2,3'.split(','), ['1', '2', '3'])

    def testUpper(self):

        self.assertEqual("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb".upper()
                                , "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
        self.assertEqual("å".upper(), 'Å')
        self.assertEqual("".upper(), "")
        self.assertEqual("%€#".upper(), "%€#")
        self.assertRaises(TypeError, str.upper, (123))

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
        self.assertEqual(re.sub("a", "b", stringProvider.testSubHelperA()), stringProvider.testSubHelperB())
        self.assertEqual(re.sub("a", "b", "a"), "b")
        self.assertEqual(re.sub("", "", ""), "")
        self.assertEqual(re.sub('@', '€€€', '@%@'), '€€€%€€€')
        self.assertRaises(TypeError, re.sub, 1, "b", "1234")
        self.assertRaises(TypeError, re.sub, "a", "b", {"kul":5})

    def testLower(self):
        self.assertEqual("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB".lower()
                                , "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
        self.assertEqual("B".lower(), 'b')
        self.assertEqual("".lower(), "")
        self.assertEqual("%€#".lower(), "%€#")
        self.assertRaises(TypeError, str.lower, (123))
        self.assertRaises(TypeError, str.lower, ({"bla" : 5}))

    def testWrap(self):

        self.assertEqual(textwrap.dedent('b').strip(), 'b')
        self.assertEqual(textwrap.dedent('').strip(), '')
        self.assertEqual(textwrap.dedent('$$$\n   $$$\n  $$$').strip(), '$$$\n   $$$\n  $$$')
        self.assertRaises(TypeError, textwrap.dedent, 123)

if __name__ == '__main__':
    unittest.main()
