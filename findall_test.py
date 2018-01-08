import re
import unittest
import stringProvider as sp

def create_result(string, num):
    result = []
    if len(string)>0:
        
        for i in range(num):
            result.append(string)
    # print (result)
    return result

class TestString(unittest.TestCase):

    def testFindall(self):
        self.assertEqual(re.findall("a","aaa"), ['a','a','a'])
        self.assertEqual(re.findall("a","bba"), ['a'])
        self.assertEqual(re.findall("a","abb"), ['a'])
        self.assertEqual(re.findall("a","bbb"), [])
        self.assertEqual(re.findall("a",""), [])
        self.assertEqual(re.findall("",""), [''])
        self.assertEqual(re.findall("aa","aaa"), ['aa'])
        self.assertEqual(re.findall("aa","aaaa"), ['aa','aa'])
        self.assertEqual(re.findall("a(b)","abab"), ['b','b'])
        self.assertEqual(re.findall("(a(b))","ab"), [('ab','b')])
        self.assertEqual(re.findall("(a(b))","abab"), [('ab','b'), ('ab','b')])
        string = sp.stringMultiply("abcde",5000)
        facit = create_result("bc",5000)
        self.assertEqual(re.findall("bc",string), facit)   

        string = sp.stringMultiply("abcde",5000)
        facit = create_result(string,1)
        self.assertEqual(re.findall(string,string), facit)  

        string = sp.stringMultiply("!#¤%&/()",5000)
        facit = create_result("#¤%",5000)
        self.assertEqual(re.findall("#¤%",string), facit)    


        string = sp.stringMultiply("abc de",5000)
        facit = create_result(" ",5000)
        self.assertEqual(re.findall(" ",string), facit)   

        with self.assertRaises(TypeError):
            self.assertEqual(re.findall(1,"111"), "111")
            self.assertEqual(re.findall("1",111), "111")
            self.assertEqual(re.findall(a,"aa"), "aa")
            self.assertEqual(re.findall("a",aa), "aa")
        
if __name__ == '__main__':
    unittest.main()