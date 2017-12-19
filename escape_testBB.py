import re
import unittest
import stringProvider

class TestString(unittest.TestCase):

    def testEscapeBB(self):

        longString = stringProvider.testSubHelperA()
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


if __name__ == '__main__':
    unittest.main()