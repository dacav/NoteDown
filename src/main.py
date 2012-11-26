#!/usr/bin/env python3

import sys
import conf
from gui import *

def main (argv=None):
    if not argv: argv = sys.argv

    # Here load from configuration file
    cfg = conf.Cfg()
    cfg.toolk = 'gtk'

    gui = notedown_gui.load(cfg)
    return gui.enter_loop()

if __name__ == '__main__':
    sys.exit(main())

