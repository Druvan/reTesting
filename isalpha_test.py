import unittest
import stringProvider as sp

class TestString(unittest.TestCase):

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

        longString = sp.stringMultiply("1234",1000000)
        self.assertFalse(longString.isalpha())
        longString = sp.stringMultiply("asdj",1000000)
        self.assertTrue(longString.isalpha())
        longString = sp.stringMultiply("¼¼¼¼",1000000)
        self.assertFalse(longString.isalpha())
        longString = sp.stringMultiply("²",1000000)
        self.assertFalse(longString.isalpha())
        
if __name__ == '__main__':
    unittest.main()