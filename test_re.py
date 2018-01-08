import unittest
import re
import stringProvider as sp

value = "aabaa"
value_caps = "aabaa AABAA"

def reg_fullmatch(pattern, text):
    if re.fullmatch(pattern, text):
        return True
    else:
        return False

def create_result(string, num):
    result = []
    if len(string) > 0:

        for i in range(num):
            result.append(string)
    # print (result)
    return result

class TestRe(unittest.TestCase):

    def testSub(self):
        self.assertEqual(re.sub("a", "b", sp.testSubHelperA()), sp.testSubHelperB())
        self.assertEqual(re.sub("a", "b", "a"), "b")
        self.assertEqual(re.sub("", "", ""), "")
        self.assertEqual(re.sub('@', '€€€', '@%@'), '€€€%€€€')
        self.assertRaises(TypeError, re.sub, 1, "b", "1234")
        self.assertRaises(TypeError, re.sub, "a", "b", {"kul": 5})


    def test_subn(self):

        self.assertEqual(re.subn("a", "b", "a"), ("b", 1))
        self.assertEqual(re.subn("a", "b", value), ("bbbbb", 4))
        self.assertEqual(re.subn("a", "b", value_caps), ("bbbbb AABAA", 4))
        self.assertEqual(re.subn("a", "b", value, 3, 1), ("bbbba", 3))
        self.assertEqual(re.subn("a", "b", "ccccc"), ("ccccc", 0))
        self.assertEqual(re.subn("", "", "",), ("", 1))
        self.assertEqual(re.subn("@", "€€€", "@%@"), ("€€€%€€€", 2))
        self.assertRaises(TypeError, re.subn, "a", 1)


    def test_search(self):

        self.assertEqual(re.search("b", value).span(), (2, 3))
        self.assertEqual(re.search("a", value).span(), (0, 1))
        self.assertEqual(re.search("c", value), None)
        self.assertEqual(re.search("1", value), None)
        self.assertEqual(re.search("", "").span(), (0, 0))
        self.assertEqual(re.search("@", "%@").span(), (1, 2))
        self.assertRaises(TypeError, re.search, "a", 1)
        self.assertRaises(TypeError, re.search, "a", True)

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

    def testFullMatch(self):
        self.assertEqual(reg_fullmatch(
            "ökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehb",
            "ökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehbökjerngöjnvöjsndvöowinefriwnrovienrbovineoirnvewoirnvåoeinrboirntbäoeirnfvxoeibienbpioenrvp9ub3p9838uegpvuibevijbve9rhå9e8rhgå0rigjbjrnfbeiubvpeurpvuehb"),
                         True)
        self.assertEqual(reg_fullmatch("x", "x"), True)
        self.assertEqual(reg_fullmatch("", ""), True)
        self.assertEqual(reg_fullmatch("1", ""), False)
        self.assertEqual(reg_fullmatch("", "1"), False)
        self.assertRaises(TypeError, reg_fullmatch, (1, ""))
        self.assertRaises(TypeError, reg_fullmatch, (True, True))
        self.assertRaises(TypeError, reg_fullmatch, ("___________", 198345093845))
        self.assertEqual(reg_fullmatch("#%&/€=", "#%&/€="), True)
        self.assertEqual(reg_fullmatch("()?", "()?"), False)

    def testFindall(self):
        self.assertEqual(re.findall("a", "aaa"), ['a', 'a', 'a'])
        self.assertEqual(re.findall("a", "bba"), ['a'])
        self.assertEqual(re.findall("a", "abb"), ['a'])
        self.assertEqual(re.findall("a", "bbb"), [])
        self.assertEqual(re.findall("a", ""), [])
        self.assertEqual(re.findall("", ""), [''])
        self.assertEqual(re.findall("aa", "aaa"), ['aa'])
        self.assertEqual(re.findall("aa", "aaaa"), ['aa', 'aa'])
        self.assertEqual(re.findall("a(b)", "abab"), ['b', 'b'])
        self.assertEqual(re.findall("(a(b))", "ab"), [('ab', 'b')])
        self.assertEqual(re.findall("(a(b))", "abab"), [('ab', 'b'), ('ab', 'b')])
        string = sp.stringMultiply("abcde", 5000)
        facit = create_result("bc", 5000)
        self.assertEqual(re.findall("bc", string), facit)

        string = sp.stringMultiply("abcde", 5000)
        facit = create_result(string, 1)
        self.assertEqual(re.findall(string, string), facit)

        string = sp.stringMultiply("!#¤%&/()", 5000)
        facit = create_result("#¤%", 5000)
        self.assertEqual(re.findall("#¤%", string), facit)

        string = sp.stringMultiply("abc de", 5000)
        facit = create_result(" ", 5000)
        self.assertEqual(re.findall(" ", string), facit)

        with self.assertRaises(TypeError):
            self.assertEqual(re.findall(1, "111"), "111")
            self.assertEqual(re.findall("1", 111), "111")
            self.assertEqual(re.findall(a, "aa"), "aa")
            self.assertEqual(re.findall("a", aa), "aa")

    def testFinditer(self):
        iter1 = re.finditer(r"\s", "a b")
        iter2 = re.finditer(r"!+", "x!y!!z!!!v")
        self.assertEqual([exclamation.group(0) for exclamation in iter2],
                         ["!", "!!", "!!!"])
        self.assertEqual(next(iter1).span(), (1, 2))

    def testEscapeBB(self):
        longString = sp.testSubHelperA()
        self.assertEqual(re.escape(""), "")
        self.assertEqual(re.escape("a"), "a")
        self.assertEqual(re.escape("!"), "\!")
        self.assertEqual(re.escape("hsdjkahsdakjhsdh"), "hsdjkahsdakjhsdh")
        self.assertEqual(re.escape("hsdjkahsdak jhsdh"), "hsdjkahsdak\\ jhsdh")
        self.assertEqual(re.escape("/hsdjkahsdakjhsdh"), "\/hsdjkahsdakjhsdh")
        self.assertEqual(re.escape("?#!"), "\?\#\!")
        self.assertEqual(re.escape("hej#san"), "hej\#san")
        self.assertEqual(re.escape("hej1020("), "hej1020\(")
        self.assertEqual(re.escape("("), "\(")
        self.assertEqual(re.escape("_("), "_\(")
        self.assertEqual(re.escape("12("), "12\(")
        self.assertEqual(re.escape("!hej1020("), "\!hej1020\(")
        self.assertEqual(re.escape("\("),
                         "\\\\\(")  # Eftersom att den "escapar" \ teckenet med \ behövs det fler \, om man printer "\\\\\(" så får man "\\\("
        self.assertEqual(re.escape(longString), longString)
        self.assertEqual(re.escape("%" + longString), "\%" + longString)
        self.assertEqual(re.escape(longString + "%"), longString + "\%")

        with self.assertRaises(TypeError):
            self.assertEqual(re.escape(1), "1")
            self.assertEqual(re.escape(), "")

        self.assertEqual(re.escape(b""), b"")
        self.assertEqual(re.escape(bytearray('a', 'ascii')), b"a")
        self.assertEqual(re.escape(bytearray('!', 'ascii')), b"\!")
        self.assertEqual(re.escape(bytearray('hsdjkahsdakjhsdh', 'ascii')), b"hsdjkahsdakjhsdh")
        self.assertEqual(re.escape(bytearray('hsdjkahsdak jhsdh', 'ascii')), b"hsdjkahsdak\\ jhsdh")
        self.assertEqual(re.escape(bytearray('/hsdjkahsdakjhsdh', 'ascii')), b"\/hsdjkahsdakjhsdh")
        self.assertEqual(re.escape(bytearray('?#!', 'ascii')), b"\?\#\!")
        self.assertEqual(re.escape(bytearray('hej1020(', 'ascii')), b"hej1020\(")
        self.assertEqual(re.escape(bytearray('_(', 'ascii')), b"_\(")
        self.assertEqual(re.escape(bytearray('!hej1020(', 'ascii')), b"\!hej1020\(")
        self.assertEqual(re.escape(bytearray('\(', 'ascii')), b"\\\\\(")
        self.assertEqual(re.escape(bytearray(longString, 'ascii')), bytearray(longString, 'ascii'))
        self.assertEqual(re.escape(bytearray("%" + longString, 'ascii')), bytearray("\%" + longString, 'ascii'))
        self.assertEqual(re.escape(bytearray(longString + "%", 'ascii')), bytearray(longString + "\%", 'ascii'))


if __name__ == '__main__':
    unittest.main()
