#!/usr/bin/env python3

from distutils.core import setup
import os, os.path

if not os.path.exists('README'):
    os.symlink('README.md', 'README')

setup(name='notedown',
      version='0.0.0',
      description='Libre WYSIWYG Markdown Editor',
      author='Giovanni Simoni',
      author_email="simgidacav@gmail.com",
      url='http://github.com/dacav/NoteDown',
      packages=[],
      license='GPLv3'
     )
