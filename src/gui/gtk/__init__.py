#!/usr/bin/env python3

from gi.repository import Gtk
from .. import notedown_gui

from . import editor, toolbar, statusbar

class Main (Gtk.Window, notedown_gui.NoteDownGui) :

    def __init__ (self, conf):
        super().__init__(title="NoteDown")
        self.set_default_size(640, 480)

        self.updating = False

        edit = editor.Editor()
        tbar = toolbar.Toolbar()
        sbar = statusbar.Statusbar()

        edit.connect('format-update', self.format_update)
        tbar.connect('format-enable', self.format_enable)
        tbar.connect('format-disable', self.format_disable)
        tbar.connect('save', self.save)
        tbar.connect('save-as', self.save_as)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        vbox.pack_start(tbar, False, False, 0)
        vbox.pack_start(edit, True, True, 0)
        vbox.pack_end(sbar, False, False, 0)

        self.add(vbox)

        self.tbar = tbar
        self.edit = edit
        self.sbar = sbar

    def format_set (self, fmt, v):
        self.edit.format_set(fmt, v)
        self.sbar.format_set(fmt, v)

    def format_enable (self, _, fmt):
        self.format_set(fmt, True)

    def format_disable (self, _, fmt):
        self.format_set(fmt, False)

    def format_update (self, edit):
        active_formats = edit.get_formats()

        self.tbar.format_update(active_formats)
        self.sbar.format_update(active_formats)

    def enter_loop (self):
        self.show_all()
        self.connect('delete-event', Gtk.main_quit)
        Gtk.main()

    def save (self, *args):
        print("savin'")

    def save_as (self, *args):
        print("savin' as")
