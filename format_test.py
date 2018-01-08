
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
        self.assertEqual('{},{},{}'.format(*longString), "a,b,a")
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
        self.assertEqual('{:=5}'.format(-3), '-   3') 
        self.assertEqual('{:=5}'.format(+3), '    3') 
        self.assertEqual('{:0=5}'.format(+3), '00003') 
        self.assertEqual('{:=5}'.format(3), '    3') 



        self.assertEqual('{:e}'.format(311111111), '3.111111e+08') 
        self.assertEqual('{:.1e}'.format(311111111), '3.1e+08') 

        self.assertEqual('{:E}'.format(311111111), '3.111111E+08') 
        self.assertEqual('{:.1E}'.format(311111111), '3.1E+08')

        self.assertEqual('{:+f} {:+f}'.format(13.37, -13.37), '+13.370000 -13.370000') 
        self.assertEqual('{: f} {: f}'.format(13.37, -13.37), ' 13.370000 -13.370000') 
        self.assertEqual('{:-f} {:-f}'.format(13.37, -13.37), '13.370000 -13.370000') 
        self.assertEqual('{:f} {:f}'.format(13.37, -13.37), '13.370000 -13.370000') 

        self.assertEqual('{:+.2f} {:+.2f}'.format(13.37, -13.37), '+13.37 -13.37') 
        self.assertEqual('{: .2f} {: .2f}'.format(13.37, -13.37), ' 13.37 -13.37') 
        self.assertEqual('{:-.2f} {:-.2f}'.format(13.37, -13.37), '13.37 -13.37') 
        self.assertEqual('{:.2f} {:.2f}'.format(13.37, -13.37), '13.37 -13.37') 

        self.assertEqual('{:+.2F} {:+.2F}'.format(13.37, -13.37), '+13.37 -13.37') 
        self.assertEqual('{: .2F} {: .2F}'.format(13.37, -13.37), ' 13.37 -13.37') 
        self.assertEqual('{:-.2F} {:-.2F}'.format(13.37, -13.37), '13.37 -13.37') 
        self.assertEqual('{:.2F} {:.2F}'.format(13.37, -13.37), '13.37 -13.37') 
        # self.assertEqual('{:.2F} {:.2F}'.format('inf', '-nan'), 'INF -NAN') Fattar inte hur den funkar

        self.assertEqual('{:.0g} {:.1g}'.format(13.37, -13.37), '1e+01 -1e+01') 
        self.assertEqual('{:.4g} {:.5g}'.format(13.37, -13.37), '13.37 -13.37') 
        self.assertEqual('{:g} {:g}'.format(13.37, -13.37), '13.37 -13.37') 
        # self.assertEqual('{:.10g} {:.17g}'.format(13.37, -13.37), '13.37 -13.37') Funkar inte för 17 och högre
        # self.assertEqual('{:.100g} {:.1000g}'.format(13.37, -13.37), '13.37 -13.37') BUGGG!!!!

        # Funkar inte för 17 eller högre
        self.assertEqual('{:.10n} {:.16n}'.format(13.37, -13.37), '13.37 -13.37') 
        self.assertEqual('{:.0n} {:.1n}'.format(13.37, -13.37), '1e+01 -1e+01') 
        self.assertEqual('{:.4n} {:.5n}'.format(13.37, -13.37), '13.37 -13.37') 
        self.assertEqual('{:n} {:n}'.format(13.37, -13.37), '13.37 -13.37') 

        self.assertEqual('{:%}'.format(13.37/-13.37), '-100.000000%') 
        self.assertEqual('{:.0%}'.format(13.37/-13.37), '-100%') 
        self.assertEqual('{:.20%}'.format(3/2), '150.00000000000000000000%') 
        self.assertEqual('{:.80%}'.format(3/2), '150.00000000000000000000000000000000000000000000000000000000000000000000000000000000%') 

        # Funkar inte för 17 eller högre
        self.assertEqual('{:.0} {:.3}'.format(13.37, -13.37), '1e+01 -13.4') 
        self.assertEqual('{:.10} {:.16}'.format(13.37, -13.37), '13.37 -13.37') 

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

        self.assertEqual('{0[2]},{0[1]},{0[0]},{1[0]},{1[1]},{1[2]}'.format((1,2,3),(4,5,6)), '3,2,1,4,5,6')


if __name__ == '__main__':
    unittest.main()