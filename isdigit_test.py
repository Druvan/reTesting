import unittest
import stringProvider as sp

class TestString(unittest.TestCase):

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

        longString = sp.stringMultiply("1234",1000000)
        self.assertTrue(longString.isdigit())
        longString = sp.stringMultiply("asdj",1000000)
        self.assertFalse(longString.isdigit())
        longString = sp.stringMultiply("¼¼¼¼",1000000)
        self.assertFalse(longString.isdigit())
        longString = sp.stringMultiply("²",1000000)
        self.assertTrue(longString.isdigit())
        
if __name__ == '__main__':
    unittest.main()