#!/usr/bin/env python3

from gi.repository import Gtk
from . import notedown_gui

class Main (Gtk.Window, notedown_gui.NoteDownGui) :

    def __init__ (self, conf):
        super().__init__(title="NoteDown")
        # More graphical stuff here

    def enter_loop (self):
        self.show_all()
        self.connect('delete-event', Gtk.main_quit)
        Gtk.main()

