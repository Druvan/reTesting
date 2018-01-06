import re
import unittest
import stringProvider

class TestString(unittest.TestCase):

    def testEscapeBB(self):

        longString = stringProvider.testSubHelperA()
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
        self.assertEqual(re.escape("\("), "\\\\\(") #Eftersom att den "escapar" \ teckenet med \ behövs det fler \, om man printer "\\\\\(" så får man "\\\("
        self.assertEqual(re.escape(longString), longString)
        self.assertEqual(re.escape("%"+longString), "\%"+longString)
        self.assertEqual(re.escape(longString+"%"), longString+"\%")

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
        self.assertEqual(re.escape(bytearray("%"+longString, 'ascii')), bytearray("\%"+longString, 'ascii'))
        self.assertEqual(re.escape(bytearray(longString+"%", 'ascii')), bytearray(longString+"\%", 'ascii'))



if __name__ == '__main__':
    unittest.main()