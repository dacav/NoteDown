#!/usr/bin/env python3

from collections import deque

class Block :
    '''
    A Block is a piece of paragraph, namely a paragraph contains one or
    more Blocks.
    '''

    def __init__ (self, text):
        self.text = text
        self.bold = False
        self.italic = False
        self.code = False

    def set_bold (self, v=True):
        self.bold = v
        if v:
            self.code = False

    def set_italic (self, v=True):
        self.italic = v
        if v:
            self.code = False

    def set_code (self, v=True):
        self.code = v
        if v:
            self.italic = False
            self.bold = False

    def __str__ (self):
        fmt = "{0}"
        if self.bold:
            fmt = "**{0}**".format(fmt)
        if self.italic:
            fmt = "*{0}*".format(fmt)
        if self.code:
            fmt = "`{0}`".format(fmt)
        return fmt.format(self.text)

    def same_format (self, other):
        if self.bold != other.bold: return False
        if self.italic != other.italic: return False
        if self.code != other.code: return False
        return True

    def join (self, other):
        self.text += ' ' + other.text

class Paragraph :

    def __init__ (self):
        self.blocks = deque()
        self.last = None
        self.quote = False
        self.code = False

    def set_quote (self, v=True):
        self.quote = v
        if v:
            self.code = False

    def set_code (self, v=True):
        self.code = v
        if v:
            self.quote = v

    def add_block (self, b):
        if self.last != None and self.last.same_format(b):
            self.last.join(b)
        else:
            self.blocks.append(b)
            self.last = b

    def __str__ (self):
        if self.code:
            def build ():
                yield '    '
                for i in self.blocks:
                    yield i.text
        else:
            def build ():
                if self.quote:
                    yield '>'
                for i in map(str, self.blocks):
                    yield i     # TODO: `yield from` as python2.3
        return ' '.join(build())

