import unittest
import stringProvider as sp

class TestString(unittest.TestCase):

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

        longString = sp.stringMultiply("1234",1000000)
        self.assertTrue(longString.isdecimal())
        
if __name__ == '__main__':
    unittest.main()