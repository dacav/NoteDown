#!/usr/bin/env python3

class NoteDownGui:
    '''
    Generalization of the gui, whatever toolkit will be used.
    '''

    pass

def load (conf):
    if conf.toolk == 'gtk':
        from . import gtk
        return gtk.Main(conf)
