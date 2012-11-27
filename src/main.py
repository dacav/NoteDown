#!/usr/bin/env python3

import sys

from core import *
import gui

def main (argv=None):
    if not argv: argv = sys.argv

    cfg = conf.Cfg()
    cfg.toolkit = 'gtk'

    gui.load(cfg).enter_loop()

    return 0

if __name__ == '__main__':
    sys.exit(main())

