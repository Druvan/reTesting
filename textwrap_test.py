import textwrap
import unittest

value = """aaaaaaaaaa
bbbbbbbbbb
cccccccccccccccccccc
"""

value_special = """€€€€€€€€€€$$$$$$$$$$
??????????
"""

value_extralong = """aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""

shorten = "aaaaa bbbbbb"
shorten_long = "aaaaaaaaaa aaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

shorten_special = "$$$$$$$$$$ $$$$$$$$$$ $$$"

empty = ''

ind  = 'aaaaa\n\n \nbbbbb'



class TestString(unittest.TestCase):


    #WRAP
    def testWrap(self):
        self.assertEqual(textwrap.wrap(value, width=10), ['aaaaaaaaaa', 'bbbbbbbbbb', 'cccccccccc', 'cccccccccc'])
        self.assertEqual(textwrap.wrap(value, width=5), ['aaaaa', 'aaaaa', 'bbbbb', 'bbbbb', 'ccccc', 'ccccc', 'ccccc', 'ccccc'])
        self.assertEqual(textwrap.wrap(value_special, width=20), ['€€€€€€€€€€$$$$$$$$$$', '??????????'])
        self.assertEqual(len(textwrap.wrap(value, width=10)), 4)
        self.assertEqual(len(textwrap.wrap(value, width=2)), 20)

    #FILL
    def testFill(self):
        self.assertEqual(textwrap.fill(value, width=10), ('aaaaaaaaaa\nbbbbbbbbbb\ncccccccccc\ncccccccccc'))
        self.assertEqual(textwrap.fill(value, width=5), ('aaaaa\naaaaa\nbbbbb\nbbbbb\nccccc\nccccc\nccccc\nccccc'))
        self.assertEqual(textwrap.fill(value_special, width=20), ('€€€€€€€€€€$$$$$$$$$$\n??????????'))
        self.assertEqual(textwrap.fill(empty, width=20), (''))
        self.assertEqual(len(textwrap.fill(value, width=10)), 43)
        self.assertEqual(len(textwrap.fill(value, width=2)), 59)

    #Shorten
    def testShorten(self):
        self.assertEqual(textwrap.shorten(shorten, width=11), 'aaaaa [...]')
        self.assertEqual(textwrap.shorten(shorten, width=10, placeholder="..."), 'aaaaa...')
        self.assertEqual(textwrap.shorten(shorten_long, width=20), 'aaaaaaaaaa [...]')
        self.assertEqual(textwrap.shorten(shorten_special, width=20), '$$$$$$$$$$ [...]')
        self.assertEqual(textwrap.shorten(empty, width=20), '')
        self.assertEqual(len(textwrap.shorten(shorten, width=11)), 11)
        self.assertEqual(len(textwrap.shorten(shorten, width=10, placeholder="...")), 8)

    #Indent
    def testIndent(self):
        self.assertEqual(textwrap.indent(ind, '+ ', lambda line: True), ('+ aaaaa\n+ \n+  \n+ bbbbb'))
        self.assertEqual(len(textwrap.indent(ind, '+ ', lambda line: True)), 22)
        self.assertEqual(len(textwrap.indent(empty, '+ ', lambda line: True)), 0)
        #self.assertEqual(len(textwrap.indent((value_extralong, '+ ', lambda line: True))), 102)
    #Dedent
    def testWrap_dedent(self):
        self.assertEqual(textwrap.dedent('b').strip(), 'b')
        self.assertEqual(textwrap.dedent('').strip(), '')
        self.assertEqual(textwrap.dedent('$$$\n   $$$\n  $$$').strip(), '$$$\n   $$$\n  $$$')
        self.assertRaises(TypeError, textwrap.dedent, 123)

if __name__ == '__main__':
    unittest.main()
