#!/usr/bin/env python3

from gi.repository import Gtk, GObject

class Toolbar (Gtk.Toolbar) :

    __gsignals__ = {
        'format-enable' : (GObject.SIGNAL_RUN_LAST, None, (str,)),
        'format-disable' : (GObject.SIGNAL_RUN_LAST, None, (str,)),
        'save' : (GObject.SIGNAL_RUN_LAST, None, tuple()),
        'save-as' : (GObject.SIGNAL_RUN_LAST, None, tuple())
    }

    def __init__ (self):
        super().__init__()

        w = dict()
        w['bold'] = Gtk.ToggleToolButton.new_from_stock(Gtk.STOCK_BOLD)
        w['italic'] = Gtk.ToggleToolButton.new_from_stock(Gtk.STOCK_ITALIC)

        for (name, btn) in w.items():
            self.add(btn)
            btn.connect('clicked', self.set_format, name)

        save = Gtk.ToolButton.new_from_stock(Gtk.STOCK_SAVE)
        save.connect('clicked', lambda *x : self.emit('save'))
        self.add(save)

        save = Gtk.ToolButton.new_from_stock(Gtk.STOCK_SAVE_AS)
        save.connect('clicked', lambda *x : self.emit('save-as'))
        self.add(save)

        self.fmt_buttons = w
        self.updating = False

    def format_update (self, active):
        self.updating = True
        for name, button  in self.fmt_buttons.items():
            button.set_active(name in active)
        self.updating = False

    def set_format (self, toggle, name):
        if not self.updating:
            if toggle.get_active():
                signal = 'format-enable'
            else:
                signal = 'format-disable'
            self.emit(signal, name)

