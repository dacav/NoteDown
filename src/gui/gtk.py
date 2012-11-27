#!/usr/bin/env python3

from gi.repository import Gtk
from . import notedown_gui

class Main (Gtk.Window, notedown_gui.NoteDownGui) :

    def __init__ (self, conf):
        super().__init__(title="NoteDown")
        self.set_default_size(640, 480)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.vbox)

        self.build_toolbar()

    def build_toolbar (self):
        tb = Gtk.Toolbar()
        self.vbox.add(tb)

        tbtn = Gtk.ToggleToolButton.new_from_stock(Gtk.STOCK_BOLD)
        tb.add(tbtn)
        tbtn.connect('clicked', self.set_style, 'bold')

        tbtn = Gtk.ToggleToolButton.new_from_stock(Gtk.STOCK_ITALIC)
        tb.add(tbtn)
        tbtn.connect('clicked', self.set_style, 'italic')

    def enter_loop (self):
        self.show_all()
        self.connect('delete-event', Gtk.main_quit)
        Gtk.main()

    def set_style (self, btn, style):
        print("{0} style {1}".format("enab" if btn.get_active() else "disab", style))
