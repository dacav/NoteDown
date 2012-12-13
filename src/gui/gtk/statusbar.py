#!/usr/bin/env python3

from gi.repository import Gtk
from collections import defaultdict as ddict
from operator import itemgetter as iget

class FormatStatus (Gtk.Label) :

    FORMATS = 'bold italic code'.split()

    def __init__ (self):
        super().__init__('')
        self.formats = ddict(lambda : False)

    def reload (self):
        flags = map(iget(0), filter(iget(1), self.formats.items()))
        self.set_text(' '.join(flags))

    def change (self, fmt, v, lock=False):
        self.formats[fmt] = v
        if not lock: self.reload()

    def update (self, active):
        for fmt in self.formats.keys():
            self.change(fmt, fmt in active, lock=True)
        self.reload()

class Statusbar (Gtk.Grid) :

    def __init__ (self):
        super().__init__()

        self.set_column_homogeneous(True)

        self.format_sb = FormatStatus()
        self.attach(self.format_sb, 2, 0, 1, 1)

    def format_set (self, fmt, v):
        self.format_sb.change(fmt, v)

    def format_update (self, active):
        self.format_sb.update(active)
