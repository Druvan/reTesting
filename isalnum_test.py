import unittest
import stringProvider as sp

class TestString(unittest.TestCase):

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

        longString = sp.stringMultiply("1234",1000000)
        self.assertTrue(longString.isalnum())
        longString = sp.stringMultiply("asdj",1000000)
        self.assertTrue(longString.isalnum())
        longString = sp.stringMultiply("¼¼¼¼",1000000)
        self.assertTrue(longString.isalnum())
        longString = sp.stringMultiply("²",1000000)
        self.assertTrue(longString.isalnum())
        
if __name__ == '__main__':
    unittest.main()