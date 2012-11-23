NoteDown
========

This project aims at building a [libre][1] WYSIWYG editor which is able to
output markdown files (something which seems to be missing on the FLOSS
scenario!)

This project is still in a project phase. I hope to be able to follow
it as I wish, as I've got just a little spare time for it :(. That said,
let's go technical.

[1]: https://en.wikipedia.org/wiki/Libre


Architecture
============

**Notedown** will be written in *Python 3*, since it fosters a rapid
development and I think it's very neat. As for the graphical interface, I
gave a glance at *PyQt4*, *tkjkk* and *Gtk3*. The latter seems IMHO the
better choice till now, but since I cannot be sure about this, I'll try to
keep the code well modularized, in order to allow subsequent replacement
(if this is needed). Besides, this could be good also in order to get
native interfaces!

I'll be giving additional details in the [wiki][2] as my idea gets
defined.

[2]: ./wiki

