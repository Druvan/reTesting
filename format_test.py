
import unittest
import stringProvider as sp

def createIndexes(input):
    result = ""
    if len(input)>0:
    
        for i in input:
            if i != input[0]:
                result = result + ","
            result = result + "{" +str(i) + "}"
        

    return result

class TestString(unittest.TestCase):

    def testFormat(self):
        longString = sp.stringMultiply("ab",10000)
        longString2 = sp.stringMultiply("hej",10000)
        inputToFormat = 'a','b','c','d','e','f','g','h'
        longStrings = "ASDKJABKSFBKAS","ASDKJABKSFBKAS","ASDKJABKSFBKAS"
        indexes = createIndexes(range(3))
        self.assertEqual('{0}'.format(*inputToFormat), "a")
        self.assertEqual('{0}'.format('a','b','c'), "a")
        self.assertEqual(indexes.format('a','b','c'), "a,b,c")
        self.assertEqual('{0},{1},{2}'.format(*longString), "a,b,a")
        self.assertEqual('{2},{1},{0}'.format(*longString), "a,b,a")
        indexes = createIndexes(range(len(longString)))
        self.assertEqual(indexes.format(*longString), sp.stringMultiply("a,b,",10000))
        last = len(longString)
        indexes = '{' +str(last-3) + '},' + '{' +str(last-2) + '},' + '{' +str(last-1) + '}' 
        self.assertEqual(indexes.format(*longString), "b,a,b")
        self.assertEqual(''.format(*inputToFormat), "")
        self.assertEqual('{0}'.format(""), "")  
        self.assertEqual('{0}'.format('%'), "%")   
        self.assertEqual('{0},{1},{2}'.format(*longStrings), "ASDKJABKSFBKAS,ASDKJABKSFBKAS,ASDKJABKSFBKAS")  
        self.assertEqual('{0},{1},{0}'.format(longString,longString2), longString+","+longString2+","+longString)  

        self.assertEqual('{test1},{test2},{test3}'.format(test1="",test2="hejsan!",test3="testerna gick igenom!"), ",hejsan!,testerna gick igenom!") 
        self.assertEqual('{test2},{test1},{test3}'.format(test1="",test2="hejsan!",test3="testerna gick igenom!"), "hejsan!,,testerna gick igenom!")
        self.assertEqual('{test2},{test3},{test1}'.format(test1="",test2="hejsan!",test3="testerna gick igenom!"), "hejsan!,testerna gick igenom!,")

        self.assertEqual('{0.real:.0f}{0.imag:.0f}'.format(15+13j), '1513')  
        self.assertEqual('{0.real:.2f}{0.imag:.2f}'.format(15+13j), '15.0013.00')

        self.assertEqual('{:<10}'.format("left"), 'left      ')  
        self.assertEqual('{:<0}'.format("left"), 'left')
        self.assertEqual('{:>10}'.format("right"), '     right')    
        self.assertEqual('{:>1}'.format("right"), 'right') 
        self.assertEqual('{:^10}'.format("center"), '  center  ') 
        self.assertEqual('{:^5}'.format("center"), 'center') 

        self.assertEqual('{:+f} {:+f}'.format(13.37, -13.37), '+13.370000 -13.370000') 
        self.assertEqual('{: f} {: f}'.format(13.37, -13.37), ' 13.370000 -13.370000') 
        self.assertEqual('{:-f} {:-f}'.format(13.37, -13.37), '13.370000 -13.370000') 
        self.assertEqual('{:f} {:f}'.format(13.37, -13.37), '13.370000 -13.370000') 
        self.assertEqual('{0:d},{0:x},{0:o},{0:b}'.format(15), '15,f,17,1111') 
        self.assertEqual('{0:d},{0:x},{0:o},{0:b}'.format(0), '0,0,0,0') 
        self.assertEqual('{0:d},{0:x},{0:o},{0:b}'.format(-2), '-2,-2,-2,-10') 
        self.assertEqual('{0:#d},{0:#x},{0:#o},{0:#b}'.format(-2), '-2,-0x2,-0o2,-0b10') 
        self.assertEqual('{:,}'.format(1000000), '1,000,000') 
        self.assertEqual('{:,}'.format(100), '100')
        self.assertEqual('{:,}'.format(1000), '1,000')
        self.assertEqual('{:,}'.format(100000), '100,000')
        self.assertEqual('{:,}'.format(-100000), '-100,000')
        self.assertEqual('{:,}'.format(0), '0')


if __name__ == '__main__':
    unittest.main()

# Accessing arguments by position:
# >>> class Point:
# ...     def __init__(self, x, y):
# ...         self.x, self.y = x, y
# ...     def __str__(self):
# ...         return 'Point({self.x}, {self.y})'.format(self=self)
# ...
# >>> str(Point(4, 2))
# 'Point(4, 2)'
# Accessing arguments’ items:

# >>> coord = (3, 5)
# >>> 'X: {0[0]};  Y: {0[1]}'.format(coord)
# 'X: 3;  Y: 5'
# Replacing %s and %r:

# >>> "repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
# "repr() shows quotes: 'test1'; str() doesn't: test2"
# Aligning the text and specifying a width:


# >>> # format also supports binary numbers
# >>> "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
# 'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
# >>> # with 0x, 0o, or 0b as prefix:
# >>> "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
# 'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'
# Using the comma as a thousands separator:

# >>> '{:,}'.format(1234567890)
# '1,234,567,890'
# Expressing a percentage:

# >>> points = 19
# >>> total = 22
# >>> 'Correct answers: {:.2%}.'.format(points/total)
# 'Correct answers: 86.36%'
# Using type-specific formatting:

# >>> import datetime
# >>> d = datetime.datetime(2010, 7, 4, 12, 15, 58)
# >>> '{:%Y-%m-%d %H:%M:%S}'.format(d)
# '2010-07-04 12:15:58'
# Nesting arguments and more complex examples:

# >>> for align, text in zip('<^>', ['left', 'center', 'right']):
# ...     '{0:{fill}{align}16}'.format(text, fill=align, align=align)
# ...
# 'left<<<<<<<<<<<<'
# '^^^^^center^^^^^'
# '>>>>>>>>>>>right'
# >>>
# >>> octets = [192, 168, 0, 1]
# >>> '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
# 'C0A80001'
# >>> int(_, 16)
# 3232235521
# >>>
# >>> width = 5
# >>> for num in range(5,12):
# ...     for base in 'dXob':
# ...         print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
# ...     print()
# ...
#     5     5     5   101
#     6     6     6   110
#     7     7     7   111
#     8     8    10  1000
#     9     9    11  1001
#    10     A    12  1010
#    11     B    13  1011