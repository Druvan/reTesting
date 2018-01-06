import unittest
import stringProvider as sp

class TestString(unittest.TestCase):

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

        longString = sp.stringMultiply("1234",1000000)
        self.assertTrue(longString.isnumeric())
        longString = sp.stringMultiply("asdj",1000000)
        self.assertFalse(longString.isnumeric())
        longString = sp.stringMultiply("¼¼¼¼",1000000)
        self.assertTrue(longString.isnumeric())
        longString = sp.stringMultiply("²",1000000)
        self.assertTrue(longString.isnumeric())
        
if __name__ == '__main__':
    unittest.main()