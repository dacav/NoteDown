#!/usr/bin/env python3

from gi.repository import Gtk
from .. import notedown_gui

from . import editor, toolbar

class Main (Gtk.Window, notedown_gui.NoteDownGui) :

    def __init__ (self, conf):
        super().__init__(title="NoteDown")
        self.set_default_size(640, 480)

        self.updating = False

        edit = editor.Editor()
        tbar = toolbar.Toolbar()
        edit.connect('format-update', tbar.update)
        tbar.connect('format-enable', edit.format_enable)
        tbar.connect('format-disable', edit.format_disable)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        vbox.add(tbar)
        vbox.add(edit)

        self.add(vbox)

    def enter_loop (self):
        self.show_all()
        self.connect('delete-event', Gtk.main_quit)
        Gtk.main()
