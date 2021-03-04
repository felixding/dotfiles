# -*- coding: utf-8 -*-
# autostart = true

import re
from xkeysnail.transform import *

#
# firefox
#
define_keymap(re.compile('firefox', re.IGNORECASE),{
    # disable alt = menu
    # https://github.com/mooz/xkeysnail/issues/43

    # copy & paste
    K("Alt-c"): K("Ctrl-c"),
    K("Alt-v"): K("Ctrl-v"),
    K("Alt-x"): K("Ctrl-x"),

    # tabs
    K("Alt-t"): K("Ctrl-t"),
    K("Alt-n"): K("Ctrl-n"),
    K("Alt-w"): K("Ctrl-w"),
    K("Alt-Right"): K("Ctrl-Page_Down"),
    K("Alt-Left"): K("Ctrl-Page_Up"),

    # new private tab
    K("Alt-Shift-p"): K("Ctrl-Shift-p"),

    # address bar
    K("Alt-l"): K("Ctrl-l"),

    # reload
    K("Alt-r"): K("Ctrl-r"),

    # app
    K("Alt-q"): K("Ctrl-Shift-q"),
    K("Alt-COMMA"): K("Ctrl-Shift-COMMA"), # remember to set it up in app's preferences

    # select all
    K("Alt-a"): K("Ctrl-a"),

    # find
    K("Alt-f"): K("Ctrl-Shift-f"),
    K("Alt-g"): K("Ctrl-Shift-g"),

    #K("Alt-a"): K("Ctrl-Shift-a"), # remember to set it up in app's preferences
    #K("Alt-h"): K("Ctrl-Shift-h"),

    # zoom
    K("Alt-MINUS"): K("Ctrl-MINUS"),
    K("Alt-EQUAL"): K("Ctrl-EQUAL"),
    K("Alt-Key_0"): K("Ctrl-Key_0"),

    #K("Alt-Key_1"): K("M-Key_1"),    # Jump to Tab #1-#8
    #K("Alt-Key_2"): K("M-Key_2"),
    #K("Alt-Key_3"): K("M-Key_3"),
    #K("Alt-Key_4"): K("M-Key_4"),
    #K("Alt-Key_5"): K("M-Key_5"),
    #K("Alt-Key_6"): K("M-Key_6"),
    #K("Alt-Key_7"): K("M-Key_7"),
    #K("Alt-Key_8"): K("M-Key_8"),
    #K("Alt-Key_9"): K("M-Key_9"),    # Jump to last tab
}, "Firefox")

#
# terminals
#
terminals = ["gnome-terminal","tilix"]
terminals = [term.casefold() for term in terminals]
termStr = "|".join(str(x) for x in terminals)

define_keymap(re.compile(termStr, re.IGNORECASE),{
    # copy & paste
    K("Alt-c"): K("Ctrl-Shift-c"),
    K("Alt-v"): K("Ctrl-Shift-v"),
    K("Alt-x"): K("Ctrl-x"),

    # tabs
    K("Alt-t"): K("Ctrl-Shift-t"),
    K("Alt-n"): K("Ctrl-Shift-n"),
    K("Alt-w"): K("Ctrl-Shift-w"),
    K("Alt-Right"): K("Ctrl-Page_Down"),
    K("Alt-Left"): K("Ctrl-Page_Up"),

    # app
    K("Alt-q"): K("Ctrl-Shift-q"),
    K("Alt-COMMA"): K("Ctrl-Shift-COMMA"), # remember to set it up in app's preferences

    # edit
    K("Alt-a"): K("Ctrl-a"),
    K("Alt-f"): K("Ctrl-Shift-f"),
    K("Alt-g"): K("Ctrl-Shift-g"),
    K("Alt-a"): K("Ctrl-Shift-a"), # remember to set it up in app's preferences
    #K("Alt-h"): K("Ctrl-Shift-h"),

    # view
    K("Alt-MINUS"): K("Ctrl-MINUS"),
    K("Alt-EQUAL"): K("Ctrl-Shift-EQUAL"),

    # for tilix
    K("Alt-Key_1"): K("Ctrl-Alt-Key_1"),    # Jump to Tab #1-#8
    K("Alt-Key_2"): K("Ctrl-Alt-Key_2"),
    K("Alt-Key_3"): K("Ctrl-Alt-Key_3"),
    K("Alt-Key_4"): K("Ctrl-Alt-Key_4"),
    K("Alt-Key_5"): K("Ctrl-Alt-Key_5"),
    K("Alt-Key_6"): K("Ctrl-Alt-Key_6"),
    K("Alt-Key_7"): K("Ctrl-Alt-Key_7"),
    K("Alt-Key_8"): K("Ctrl-Alt-Key_8"),
    K("Alt-Key_9"): K("Ctrl-Alt-Key_9"),    # Jump to last tab
}, "terminals")
