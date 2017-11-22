import re
import unittest

class TestString(unittest.TestCase):

    def BlackBox(self):
    
        self.assertEqual( re.escape(""), "")
        self.assertEqual( re.escape("hsdjkahsdakjhsdh"), "hsdjkahsdakjhsdh")
        self.assertEqual( re.escape("/hsdjkahsdakjhsdh"), "\/hsdjkahsdakjhsdh")
        self.assertEqual( re.escape("?#!"), "\?\#\!")
        self.assertEqual( re.escape("hej#san"), "hej\#san")
        self.assertEqual( re.escape("hej1020("), "hej1020\(")
        self.assertEqual( re.escape("("), "\(")
        self.assertEqual( re.escape("_("), "_\(")
        self.assertEqual( re.escape("12("), "12\(")
        self.assertEqual( re.escape("!hej1020("), "\!hej1020\(")
        self.assertEqual( re.escape("\("), "\\(")
        
        
        
        
        
        


if __name__ == '__main__':
    unittest.main()