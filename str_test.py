import unittest
import stringProvider as sp


class str_test(unittest.TestCase):
    
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

    def testLower(self):
        self.assertEqual("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB".lower()
                                , "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
        self.assertEqual("B".lower(), 'b')
        self.assertEqual("".lower(), "")
        self.assertEqual("%€#".lower(), "%€#")
        self.assertRaises(TypeError, str.lower, (123))
        self.assertRaises(TypeError, str.lower, ({"bla" : 5}))



if __name__ == '__main__':
    unittest.main()
