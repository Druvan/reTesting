import unittest

_alphanum_str = set('_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890')
_alphanum_bytes = set(b'_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890')

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
    def testEscapeWB(self):
        self.assertEqual(escape(""), "")
        self.assertEqual(escape("python.exe"), "python\.exe")
        self.assertEqual(escape("\00"), "\\000")

        self.assertEqual(escape(bytearray(1)), b"\\000")
        self.assertEqual(escape(bytearray('hej', 'ascii')), b"hej")
        self.assertEqual(escape(bytearray('he\b', 'ascii')), b'he\\\x08')
if __name__ == '__main__':
    unittest.main()