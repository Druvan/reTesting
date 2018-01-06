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

shorten = "aaaaa bbbbbb"
shorten_long = "aaaaaaaaaa aaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


class TestString(unittest.TestCase):

    #WRAP
    def testWrap(self): 
        self.assertEqual(textwrap.wrap(value, width=10), ['aaaaaaaaaa', 'bbbbbbbbbb', 'cccccccccc', 'cccccccccc'])
        self.assertEqual(textwrap.wrap(value, width=5), ['aaaaa', 'aaaaa', 'bbbbb', 'bbbbb', 'ccccc', 'ccccc', 'ccccc', 'ccccc'])
        self.assertEqual(textwrap.wrap(value_long, width=20), ['aaaaaaaaaabbbbbbbbbb', 'cccccccccccccccccccc'])
        self.assertEqual(len(textwrap.wrap(value, width=10)), 4)
        self.assertEqual(len(textwrap.wrap(value, width=2)), 20)

    #FILL    
    def testFill(self):
        self.assertEqual(textwrap.fill(value, width=10), ('aaaaaaaaaa\nbbbbbbbbbb\ncccccccccc\ncccccccccc'))
        self.assertEqual(textwrap.fill(value, width=5), ('aaaaa\naaaaa\nbbbbb\nbbbbb\nccccc\nccccc\nccccc\nccccc'))
        self.assertEqual(textwrap.fill(value_long, width=20), ('aaaaaaaaaabbbbbbbbbb\ncccccccccccccccccccc'))
        self.assertEqual(len(textwrap.fill(value, width=10)), 43)
        self.assertEqual(len(textwrap.fill(value, width=2)), 59)

    #Shorten
    def testShorten(self):
        self.assertEqual(textwrap.shorten(shorten, width=11), 'aaaaa [...]')
        self.assertEqual(textwrap.shorten(shorten, width=10, placeholder="..."), 'aaaaa...')
        self.assertEqual(textwrap.shorten(shorten_long, width=20), 'aaaaaaaaaa [...]')
        self.assertEqual(len(textwrap.shorten(shorten, width=11)), 11)
        self.assertEqual(len(textwrap.shorten(shorten, width=10, placeholder="...")), 8)
        
        
        

if __name__ == '__main__':
   unittest.main()
