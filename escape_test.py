import re
import unittest

def escape(pattern):
    """
    Escape all the characters in pattern except ASCII letters, numbers and '_'.
    """
    if isinstance(pattern, str):
        alphanum = _alphanum_str
        s = list(pattern)
        for i, c in enumerate(pattern):
            if c not in alphanum:
                if c == "\000":
                    s[i] = "\\000"
                else:
                    s[i] = "\\" + c
        return "".join(s)
    else:
        alphanum = _alphanum_bytes
        s = []
        esc = ord(b"\\")
        for c in pattern:
            if c in alphanum:
                s.append(c)
            else:
                if c == 0:
                    s.extend(b"\\000")
                else:
                    s.append(esc)
                    s.append(c)
        return bytes(s)


class TestString(unittest.TestCase):

    def escapeBB(self):
    
        self.assertEqual(re.escape("a"), "")
        self.assertEqual(re.escape("hsdjkahsdakjhsdh"), "hsdjkahsdakjhsdh")
        self.assertEqual(re.escape("hsdjkahsdak jhsdh"), "hsdjkahsdak jhsdh")
        self.assertEqual(re.escape("/hsdjkahsdakjhsdh"), "\/hsdjkahsdakjhsdh")
        self.assertEqual(re.escape("?#!"), "\?\#!")
        self.assertEqual(re.escape("hej#san"), "hej\#san")
        self.assertEqual(re.escape("hej1020("), "hej1020\(")
        self.assertEqual(re.escape("("), "\(")
        self.assertEqual(re.escape("_("), "_\(")
        self.assertEqual(re.escape("12("), "12\(")
        self.assertEqual(re.escape("!hej1020("), "\!hej1020\(")
        self.assertEqual(re.escape("\("), "\\(")

    """"
    def escapeWB(self):
        self.assertEqual(re.escape(""), "")
        self.assertEqual(re.escape("python.exe"), "python\.exe")
        self.assertEqual(re.escape("a null" + None + "inbetween"), "a null \\000 inbetween")
    """

    def escapeWB(self):
            self.assertEqual(escape(""), "")
            self.assertEqual(escape("python.exe"), "python\.exe")
            self.assertEqual(escape("a null" + None + "inbetween"), "a null \\000 inbetween")


    if __name__ == '__main__':
        unittest.main()