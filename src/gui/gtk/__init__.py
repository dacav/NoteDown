#!/usr/bin/env python3

from gi.repository import Gtk, Pango
from .. import notedown_gui

from . import editor

class Main (Gtk.Window, notedown_gui.NoteDownGui) :

    def __init__ (self, conf):
        super().__init__(title="NoteDown")
        self.set_default_size(640, 480)

        self.updating = False

        self.editor = editor.Editor()
        self.editor.connect('format-update', self.update_toolbar)
        self.build_toolbar()

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        vbox.add(self.toolbar)
        vbox.add(self.editor)
        self.add(vbox)

    def build_toolbar (self):
        btns = dict()
        tb = Gtk.Toolbar()

        tbtn = Gtk.ToggleToolButton.new_from_stock(Gtk.STOCK_BOLD)
        tb.add(tbtn)
        btns['bold'] = tbtn;

        tbtn = Gtk.ToggleToolButton.new_from_stock(Gtk.STOCK_ITALIC)
        tb.add(tbtn)
        btns['italic'] = tbtn

        for (name, btn) in btns.items():
            btn.connect('clicked', self.set_format, name)

        self.toolbar = tb
        self.fmt_buttons = btns;

    def update_toolbar (self, editor):
        active = editor.get_formats()
        self.updating = True
        for name, button  in self.fmt_buttons.items():
            button.set_active(name in active)
        self.updating = False

    def enter_loop (self):
        self.show_all()
        self.connect('delete-event', Gtk.main_quit)
        Gtk.main()

    def set_format (self, btn, fmt):
        if not self.updating:
            self.editor.set_format(fmt, btn.get_active())

