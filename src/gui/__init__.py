#!/usr/bin/env python3

def load (conf):
    if conf.toolkit == 'gtk':
        from . import gtk
        return gtk.Main(conf)

