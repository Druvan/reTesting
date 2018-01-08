import unittest
import string
import stringProvider as sp

str_1 = "Line1- a\n\nLine3- b\nLine4- c"
str_2 = "Line1- a\n\nLine3- b\nLine4- cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
str_3 = "\n\n"
str_4 = ""
str_5 = "000AAAAA000"
str_6 = "AAAAA000"


def createIndexes(input):
    result = ""
    if len(input) > 0:

        for i in input:
            if i != input[0]:
                result = result + ","
            result = result + "{" + str(i) + "}"

    return result

class TestString(unittest.TestCase):

    def testSplit(self):
        self.assertEqual('a'.split(','), ['a'])
        self.assertEqual(''.split(','), [''])
        self.assertEqual("@,#,€".split(','), ['@', '#', '€'])
        self.assertEqual('1,2,3'.split('k'), ['1,2,3'])
        self.assertRaises(TypeError, '1,2'.split, 3)
        self.assertRaises(ValueError, ''.split, '')
        self.assertEqual('1,2,3'.split(','), ['1', '2', '3'])

    def test_splitlines(self):
        self.assertEqual(str_1.splitlines(), ["Line1- a", "", "Line3- b", "Line4- c"])
        self.assertEqual(str_1.splitlines(True), ["Line1- a\n", "\n", "Line3- b\n", "Line4- c"])
        self.assertEqual(str_2.splitlines(), ["Line1- a", "", "Line3- b", "Line4- cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"])
        self.assertEqual(str_3.splitlines(), ["",""])
        self.assertEqual(str_3.splitlines(True), ["\n", "\n"])
        self.assertEqual(str_4.splitlines(), [])
        self.assertEqual(str_4.splitlines(True), [])
        self.assertRaises(TypeError, str_1.splitlines, True, "b")
        self.assertRaises(TypeError, str_1.splitlines, True, "@")
        self.assertRaises(TypeError, str_1.splitlines, True, 1)

    def test_Strip(self):
        self.assertEqual(str_5.strip("0"), "AAAAA")
        self.assertEqual(str_5.strip("1"), "000AAAAA000")
        self.assertEqual(str_5.strip("@"), "000AAAAA000")
        self.assertEqual(str_6.strip("0"), "AAAAA")
        self.assertEqual(str_5.strip(""), "000AAAAA000")
        self.assertRaises(TypeError, str_5.strip, "a", 1)
        self.assertRaises(TypeError, str_5.strip, "a", True)

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
        self.assertRaises(TypeError, str.lower, ({"bla": 5}))

    def testIsdigit(self):
        self.assertFalse("a".isdigit())
        self.assertFalse("%".isdigit())
        self.assertFalse("".isdigit())
        self.assertFalse(" ".isdigit())
        self.assertFalse(bin(10).isdigit())
        self.assertFalse(hex(10).isdigit())
        self.assertFalse(oct(10).isdigit())

        self.assertTrue("1".isdigit())
        self.assertTrue("0".isdigit())
        self.assertFalse("¼".isdigit())
        self.assertTrue("²".isdigit())

        self.assertFalse("-1".isdigit())
        self.assertFalse("(-1)".isdigit())
        self.assertFalse("1.0".isdigit())

        longString = sp.stringMultiply("1234", 1000000)
        self.assertTrue(longString.isdigit())
        longString = sp.stringMultiply("asdj", 1000000)
        self.assertFalse(longString.isdigit())
        longString = sp.stringMultiply("¼¼¼¼", 1000000)
        self.assertFalse(longString.isdigit())
        longString = sp.stringMultiply("²", 1000000)
        self.assertTrue(longString.isdigit())

    def testIsdecimal(self):
        self.assertFalse("a".isdecimal())
        self.assertFalse("%".isdecimal())
        self.assertFalse("".isdecimal())
        self.assertFalse(" ".isdecimal())
        self.assertFalse(bin(10).isdecimal())
        self.assertFalse(hex(10).isdecimal())
        self.assertFalse(oct(10).isdecimal())

        self.assertTrue("1".isdecimal())
        self.assertTrue("0".isdecimal())
        self.assertFalse("¼".isdigit())
        self.assertTrue("²".isdigit())

        self.assertFalse("-1".isdecimal())
        self.assertFalse("(-1)".isdecimal())
        self.assertFalse("1.0".isdecimal())

        longString = sp.stringMultiply("1234", 1000000)
        self.assertTrue(longString.isdecimal())

    def testIsalpha(self):
        self.assertTrue("a".isalpha())
        self.assertFalse("%".isalpha())
        self.assertFalse("".isalpha())
        self.assertFalse(" ".isalpha())
        self.assertFalse(bin(10).isalpha())
        self.assertFalse(hex(10).isalpha())
        self.assertFalse(oct(10).isalpha())

        self.assertFalse("1".isalpha())
        self.assertFalse("0".isalpha())
        self.assertFalse("¼".isalpha())
        self.assertFalse("²".isalpha())

        self.assertFalse("-1".isalpha())
        self.assertFalse("(-1)".isalpha())
        self.assertFalse("1.0".isalpha())

        longString = sp.stringMultiply("1234", 1000000)
        self.assertFalse(longString.isalpha())
        longString = sp.stringMultiply("asdj", 1000000)
        self.assertTrue(longString.isalpha())
        longString = sp.stringMultiply("¼¼¼¼", 1000000)
        self.assertFalse(longString.isalpha())
        longString = sp.stringMultiply("²", 1000000)
        self.assertFalse(longString.isalpha())

    def testIsnumeric(self):
        self.assertFalse("a".isnumeric())
        self.assertFalse("%".isnumeric())
        self.assertFalse("".isnumeric())
        self.assertFalse(" ".isnumeric())
        self.assertFalse(bin(10).isnumeric())
        self.assertFalse(hex(10).isnumeric())
        self.assertFalse(oct(10).isnumeric())

        self.assertTrue("1".isnumeric())
        self.assertTrue("0".isnumeric())
        self.assertTrue("¼".isnumeric())
        self.assertTrue("²".isnumeric())

        self.assertFalse("-1".isnumeric())
        self.assertFalse("(-1)".isnumeric())
        self.assertFalse("1.0".isnumeric())

        longString = sp.stringMultiply("1234", 1000000)
        self.assertTrue(longString.isnumeric())
        longString = sp.stringMultiply("asdj", 1000000)
        self.assertFalse(longString.isnumeric())
        longString = sp.stringMultiply("¼¼¼¼", 1000000)
        self.assertTrue(longString.isnumeric())
        longString = sp.stringMultiply("²", 1000000)
        self.assertTrue(longString.isnumeric())

    def testIsalnum(self):
        self.assertTrue("a".isalnum())
        self.assertFalse("%".isalnum())
        self.assertFalse("".isalnum())
        self.assertFalse(" ".isalnum())
        self.assertTrue(bin(10).isalnum())
        self.assertTrue(hex(10).isalnum())
        self.assertTrue(oct(10).isalnum())

        self.assertTrue("1".isalnum())
        self.assertTrue("0".isalnum())
        self.assertTrue("¼".isalnum())
        self.assertTrue("²".isalnum())

        self.assertFalse("-1".isalnum())
        self.assertFalse("(-1)".isalnum())
        self.assertFalse("1.0".isalnum())

        longString = sp.stringMultiply("1234", 1000000)
        self.assertTrue(longString.isalnum())
        longString = sp.stringMultiply("asdj", 1000000)
        self.assertTrue(longString.isalnum())
        longString = sp.stringMultiply("¼¼¼¼", 1000000)
        self.assertTrue(longString.isalnum())
        longString = sp.stringMultiply("²", 1000000)
        self.assertTrue(longString.isalnum())

    def testFormat(self):
        longString = sp.stringMultiply("ab", 10000)
        longString2 = sp.stringMultiply("hej", 10000)
        inputToFormat = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
        longStrings = "ASDKJABKSFBKAS", "ASDKJABKSFBKAS", "ASDKJABKSFBKAS"
        indexes = createIndexes(range(3))
        self.assertEqual('{0}'.format(*inputToFormat), "a")
        self.assertEqual('{0}'.format('a', 'b', 'c'), "a")
        self.assertEqual(indexes.format('a', 'b', 'c'), "a,b,c")
        self.assertEqual('{0},{1},{2}'.format(*longString), "a,b,a")
        self.assertEqual('{},{},{}'.format(*longString), "a,b,a")
        self.assertEqual('{2},{1},{0}'.format(*longString), "a,b,a")
        indexes = createIndexes(range(len(longString)))
        self.assertEqual(indexes.format(*longString), sp.stringMultiply("a,b,", 10000))
        last = len(longString)
        indexes = '{' + str(last - 3) + '},' + '{' + str(last - 2) + '},' + '{' + str(last - 1) + '}'
        self.assertEqual(indexes.format(*longString), "b,a,b")
        self.assertEqual(''.format(*inputToFormat), "")
        self.assertEqual('{0}'.format(""), "")
        self.assertEqual('{0}'.format('%'), "%")
        self.assertEqual('{0},{1},{2}'.format(*longStrings), "ASDKJABKSFBKAS,ASDKJABKSFBKAS,ASDKJABKSFBKAS")
        self.assertEqual('{0},{1},{0}'.format(longString, longString2),
                         longString + "," + longString2 + "," + longString)

        self.assertEqual('{test1},{test2},{test3}'.format(test1="", test2="hejsan!", test3="testerna gick igenom!"),
                         ",hejsan!,testerna gick igenom!")
        self.assertEqual('{test2},{test1},{test3}'.format(test1="", test2="hejsan!", test3="testerna gick igenom!"),
                         "hejsan!,,testerna gick igenom!")
        self.assertEqual('{test2},{test3},{test1}'.format(test1="", test2="hejsan!", test3="testerna gick igenom!"),
                         "hejsan!,testerna gick igenom!,")

        self.assertEqual('{0.real:.0f}{0.imag:.0f}'.format(15 + 13j), '1513')
        self.assertEqual('{0.real:.2f}{0.imag:.2f}'.format(15 + 13j), '15.0013.00')

        self.assertEqual('{:<10}'.format("left"), 'left      ')
        self.assertEqual('{:<0}'.format("left"), 'left')
        self.assertEqual('{:>10}'.format("right"), '     right')
        self.assertEqual('{:>1}'.format("right"), 'right')
        self.assertEqual('{:^10}'.format("center"), '  center  ')
        self.assertEqual('{:^5}'.format("center"), 'center')
        self.assertEqual('{:=5}'.format(-3), '-   3')
        self.assertEqual('{:=5}'.format(+3), '    3')
        self.assertEqual('{:0=5}'.format(+3), '00003')
        self.assertEqual('{:=5}'.format(3), '    3')

        self.assertEqual('{:e}'.format(311111111), '3.111111e+08')
        self.assertEqual('{:.1e}'.format(311111111), '3.1e+08')

        self.assertEqual('{:E}'.format(311111111), '3.111111E+08')
        self.assertEqual('{:.1E}'.format(311111111), '3.1E+08')

        self.assertEqual('{:+f} {:+f}'.format(13.37, -13.37), '+13.370000 -13.370000')
        self.assertEqual('{: f} {: f}'.format(13.37, -13.37), ' 13.370000 -13.370000')
        self.assertEqual('{:-f} {:-f}'.format(13.37, -13.37), '13.370000 -13.370000')
        self.assertEqual('{:f} {:f}'.format(13.37, -13.37), '13.370000 -13.370000')

        self.assertEqual('{:+.2f} {:+.2f}'.format(13.37, -13.37), '+13.37 -13.37')
        self.assertEqual('{: .2f} {: .2f}'.format(13.37, -13.37), ' 13.37 -13.37')
        self.assertEqual('{:-.2f} {:-.2f}'.format(13.37, -13.37), '13.37 -13.37')
        self.assertEqual('{:.2f} {:.2f}'.format(13.37, -13.37), '13.37 -13.37')

        self.assertEqual('{:+.2F} {:+.2F}'.format(13.37, -13.37), '+13.37 -13.37')
        self.assertEqual('{: .2F} {: .2F}'.format(13.37, -13.37), ' 13.37 -13.37')
        self.assertEqual('{:-.2F} {:-.2F}'.format(13.37, -13.37), '13.37 -13.37')
        self.assertEqual('{:.2F} {:.2F}'.format(13.37, -13.37), '13.37 -13.37')
        # self.assertEqual('{:.2F} {:.2F}'.format('inf', '-nan'), 'INF -NAN') Fattar inte hur den funkar

        self.assertEqual('{:.0g} {:.1g}'.format(13.37, -13.37), '1e+01 -1e+01')
        self.assertEqual('{:.4g} {:.5g}'.format(13.37, -13.37), '13.37 -13.37')
        self.assertEqual('{:g} {:g}'.format(13.37, -13.37), '13.37 -13.37')
        # self.assertEqual('{:.10g} {:.17g}'.format(13.37, -13.37), '13.37 -13.37') Funkar inte för 17 och högre
        # self.assertEqual('{:.100g} {:.1000g}'.format(13.37, -13.37), '13.37 -13.37') BUGGG!!!!

        # Funkar inte för 17 eller högre
        self.assertEqual('{:.10n} {:.16n}'.format(13.37, -13.37), '13.37 -13.37')
        self.assertEqual('{:.0n} {:.1n}'.format(13.37, -13.37), '1e+01 -1e+01')
        self.assertEqual('{:.4n} {:.5n}'.format(13.37, -13.37), '13.37 -13.37')
        self.assertEqual('{:n} {:n}'.format(13.37, -13.37), '13.37 -13.37')

        self.assertEqual('{:%}'.format(13.37 / -13.37), '-100.000000%')
        self.assertEqual('{:.0%}'.format(13.37 / -13.37), '-100%')
        self.assertEqual('{:.20%}'.format(3 / 2), '150.00000000000000000000%')
        self.assertEqual('{:.80%}'.format(3 / 2),
                         '150.00000000000000000000000000000000000000000000000000000000000000000000000000000000%')

        # Funkar inte för 17 eller högre
        self.assertEqual('{:.0} {:.3}'.format(13.37, -13.37), '1e+01 -13.4')
        self.assertEqual('{:.10} {:.16}'.format(13.37, -13.37), '13.37 -13.37')

        self.assertEqual('{0:d},{0:x},{0:o},{0:b}'.format(15), '15,f,17,1111')
        self.assertEqual('{0:d},{0:x},{0:o},{0:b}'.format(0), '0,0,0,0')
        self.assertEqual('{0:d},{0:x},{0:o},{0:b}'.format(-2), '-2,-2,-2,-10')
        self.assertEqual('{0:#d},{0:#x},{0:#o},{0:#b}'.format(-2), '-2,-0x2,-0o2,-0b10')
        self.assertEqual('{:,}'.format(1000000), '1,000,000')
        self.assertEqual('{:,}'.format(100), '100')
        self.assertEqual('{:,}'.format(1000), '1,000')
        self.assertEqual('{:,}'.format(100000), '100,000')
        self.assertEqual('{:,}'.format(-100000), '-100,000')
        self.assertEqual('{:,}'.format(0), '0')

        self.assertEqual('{0[2]},{0[1]},{0[0]},{1[0]},{1[1]},{1[2]}'.format((1, 2, 3), (4, 5, 6)), '3,2,1,4,5,6')



if __name__ == '__main__':
    unittest.main()
