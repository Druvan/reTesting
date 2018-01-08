import unittest
import stringProvider
import re

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
        
class re_test(unittest.TestCase):
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
    #DONE
    def testSub(self):
        self.assertEqual(re.sub("a", "b", stringProvider.testSubHelperA()), stringProvider.testSubHelperB())
        self.assertEqual(re.sub("a", "b", "a"), "b")
        self.assertEqual(re.sub("", "", ""), "")
        self.assertEqual(re.sub('@', '€€€', '@%@'), '€€€%€€€')
        self.assertRaises(TypeError, re.sub, 1, "b", "1234")
        self.assertRaises(TypeError, re.sub, "a", "b", {"kul":5})

 #Finditer    
    def testFinditer(self):
        iter1 = re.finditer(r"\s", "a b")
        iter2 = re.finditer(r"!+", "x!y!!z!!!v")
        self.assertEqual([exclamation.group(0) for exclamation in iter2],
                         ["!", "!!", "!!!"])
        self.assertEqual(next(iter1).span(), (1,2))

if __name__ == '__main__':
    unittest.main()
