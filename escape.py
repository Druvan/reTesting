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
