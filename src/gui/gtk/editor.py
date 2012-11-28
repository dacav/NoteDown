#!/usr/bin/env python3

from gi.repository import Gtk, Pango, GObject

class Editor (Gtk.TextView) :

    __gsignals__ = {
        'format-update' : (GObject.SIGNAL_RUN_LAST, None, tuple())
    }

    def __init__ (self):
        super().__init__()

        buf = self.get_buffer()
        buf.create_tag('bold', weight=Pango.Weight.BOLD)
        buf.create_tag('italic', style=Pango.Style.ITALIC)
        buf.create_tag('debug', background='yellow')
        self.buffer = buf

        emit = lambda *x : self.emit('format-update')
        buf.connect("mark-set", emit)

    def current_iter (self):
        return self.buffer.get_iter_at_mark(self.buffer.get_insert())

    def get_formats (self):
        tags = self.current_iter().get_tags()
        return set(t.get_property('name') for t in tags)

    def current_word (self):
        cur = self.current_iter()
        state = (cur.starts_word(), cur.inside_word(), cur.ends_word())
        if not any(state):
            return (cur, cur)
        if all(state):
            state = (False, False)
        else:
            state = (state[0], state[2])

        start = cur.copy()
        if not state[0]:
            start.backward_word_start()

        if not state[1]:
            cur.forward_word_end()

        return (start, cur)

    def format_set (self, fmt, val):
        bounds = self.buffer.get_selection_bounds()
        if bounds:
            start, end = bounds
        else:
            start, end = self.current_word()
        if val:
            self.buffer.apply_tag_by_name(fmt, start, end)
        else:
            self.buffer.remove_tag_by_name(fmt, start, end)

    def format_disable (self, _, fmt):
        self.format_set(fmt, False)

    def format_enable (self, _, fmt):
        self.format_set(fmt, True)
