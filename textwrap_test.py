import textwrap
import unittest

value = """aaaaaaaaaa
bbbbbbbbbb
cccccccccccccccccccc
"""

value_long = """aaaaaaaaaabbbbbbbbbb
cccccccccccccccccccc
"""

value_extralong = """aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""


wrap_extralong = textwrap.wrap(value, width=1)
print(len(value_extralong))
print(len(wrap_extralong))

# Wrap this text.
list = textwrap.wrap(value, width=10)

# Print each line.
for element in list:
    print(element)

class TestString(unittest.TestCase):

    
    def testWrap(self): 
        self.assertEqual(textwrap.wrap(value, width=10), ['aaaaaaaaaa', 'bbbbbbbbbb', 'cccccccccc', 'cccccccccc'])
        self.assertEqual(textwrap.wrap(value, width=5), ['aaaaa', 'aaaaa', 'bbbbb', 'bbbbb', 'ccccc', 'ccccc', 'ccccc', 'ccccc'])
        self.assertEqual(textwrap.wrap(value_long, width=20), ['aaaaaaaaaabbbbbbbbbb', 'cccccccccccccccccccc'])
        self.assertEqual(len(textwrap.wrap(value, width=10)), 4)
        self.assertEqual(len(textwrap.wrap(value, width=2)), 20)
    
        
      


if __name__ == '__main__':
   unittest.main()
