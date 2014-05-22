import re

class Input(object):
    def __init__(self):
        self.buffer = []
    def match_multiline(self, pattern, line):
        if re.match(pattern, line):
            if self.buffer:
                data = "".join(self.buffer)
                self.buffer = []
                return data
            self.buffer = [line]
            return None
        if self.buffer:
            self.buffer.append(line)
            return None
        return None
    def match_line(self, pattern, line):
        m = re.match(pattern, line)
        if m:
            try:
                return m.groupdict()
            except AttributeError:
                return line
        return None
