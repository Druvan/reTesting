import re
import unittest

class TestString(unittest.TestCase):

    def escapeBB(self):
    
        self.assertEqual(re.escape("a"), "")
        self.assertEqual(re.escape("hsdjkahsdakjhsdh"), "hsdjkahsdakjhsdh")
        self.assertEqual(re.escape("hsdjkahsdak jhsdh"), "hsdjkahsdak jhsdh")
        self.assertEqual(re.escape("/hsdjkahsdakjhsdh"), "\/hsdjkahsdakjhsdh")
        self.assertEqual(re.escape("?#!"), "\?\#!")
        self.assertEqual(re.escape("hej#san"), "hej\#san")
        self.assertEqual(re.escape("hej1020("), "hej1020\(")
        self.assertEqual(re.escape("("), "\(")
        self.assertEqual(re.escape("_("), "_\(")
        self.assertEqual(re.escape("12("), "12\(")
        self.assertEqual(re.escape("!hej1020("), "\!hej1020\(")
        self.assertEqual(re.escape("\("), "\\(")
        
    def escapeWB(self):
        self.assertEqual(re.escape(""), "")
        self.assertEqual(re.escape("python.exe"), "python\.exe")
        self.assertEqual(re.escape("a null" + None + "inbetween"), "a null \\000 inbetween")


    if __name__ == '__main__':
        unittest.main()