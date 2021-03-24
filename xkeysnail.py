# -*- coding: utf-8 -*-
# autostart = true

import re
from xkeysnail.transform import *

#
# global
#
modifier_key = "Super"

#
# firefox
#
define_keymap(re.compile('firefox', re.IGNORECASE),{
    # disable alt = menu
    # https://github.com/mooz/xkeysnail/issues/43

    # copy & paste
    K(f"{modifier_key}-c"): K("Ctrl-c"),
    K(f"{modifier_key}-v"): K("Ctrl-v"),
    K(f"{modifier_key}-x"): K("Ctrl-x"),

    # tabs
    K(f"{modifier_key}-t"): K("Ctrl-t"),
    K(f"{modifier_key}-n"): K("Ctrl-n"),
    K(f"{modifier_key}-w"): K("Ctrl-w"),
    K(f"{modifier_key}-Right"): K("Ctrl-Page_Down"),
    K(f"{modifier_key}-Left"): K("Ctrl-Page_Up"),

    # new private tab
    K(f"{modifier_key}-Shift-p"): K("Ctrl-Shift-p"),

    # address bar
    K(f"{modifier_key}-l"): K("Ctrl-l"),

    # reload
    K(f"{modifier_key}-r"): K("Ctrl-r"),

    # app
    K(f"{modifier_key}-q"): K("Ctrl-Shift-q"),
    K(f"{modifier_key}-COMMA"): K("Ctrl-Shift-COMMA"), # remember to set it up in app's preferences

    # select all
    K(f"{modifier_key}-a"): K("Ctrl-a"),

    # find
    K(f"{modifier_key}-f"): K("Ctrl-Shift-f"),
    K(f"{modifier_key}-g"): K("Ctrl-Shift-g"),

    #K(f"{modifier_key}-a"): K("Ctrl-Shift-a"), # remember to set it up in app's preferences
    #K(f"{modifier_key}-h"): K("Ctrl-Shift-h"),

    # zoom
    K(f"{modifier_key}-MINUS"): K("Ctrl-MINUS"),
    K(f"{modifier_key}-EQUAL"): K("Ctrl-EQUAL"),
    K(f"{modifier_key}-Key_0"): K("Ctrl-Key_0"),

    #K(f"{modifier_key}-Key_1"): K("M-Key_1"),    # Jump to Tab #1-#8
    #K(f"{modifier_key}-Key_2"): K("M-Key_2"),
    #K(f"{modifier_key}-Key_3"): K("M-Key_3"),
    #K(f"{modifier_key}-Key_4"): K("M-Key_4"),
    #K(f"{modifier_key}-Key_5"): K("M-Key_5"),
    #K(f"{modifier_key}-Key_6"): K("M-Key_6"),
    #K(f"{modifier_key}-Key_7"): K("M-Key_7"),
    #K(f"{modifier_key}-Key_8"): K("M-Key_8"),
    #K(f"{modifier_key}-Key_9"): K("M-Key_9"),    # Jump to last tab
}, "Firefox")

#
# terminals
#
terminals = ["gnome-terminal","tilix"]
terminals = [term.casefold() for term in terminals]
termStr = "|".join(str(x) for x in terminals)

define_keymap(re.compile(termStr, re.IGNORECASE),{
    # copy & paste
    #K(f"{modifier_key}-c"): K("Ctrl-Shift-c"),
    K(f"{modifier_key}-c"): K("Ctrl-Shift-c"),
    K(f"{modifier_key}-v"): K("Ctrl-Shift-v"),
    K(f"{modifier_key}-x"): K("Ctrl-x"),

    # tabs
    K(f"{modifier_key}-t"): K("Ctrl-Shift-t"),
    K(f"{modifier_key}-n"): K("Ctrl-Shift-n"),
    K(f"{modifier_key}-w"): K("Ctrl-Shift-w"),
    K(f"{modifier_key}-Right"): K("Ctrl-Page_Down"),
    K(f"{modifier_key}-Left"): K("Ctrl-Page_Up"),

    # app
    K(f"{modifier_key}-q"): K("Ctrl-Shift-q"),
    K(f"{modifier_key}-COMMA"): K("Ctrl-Shift-COMMA"), # remember to set it up in app's preferences

    # edit
    K(f"{modifier_key}-a"): K("Ctrl-a"),
    K(f"{modifier_key}-f"): K("Ctrl-Shift-f"),
    K(f"{modifier_key}-g"): K("Ctrl-Shift-g"),
    K(f"{modifier_key}-a"): K("Ctrl-Shift-a"), # remember to set it up in app's preferences
    #K(f"{modifier_key}-h"): K("Ctrl-Shift-h"),

    # view
    K(f"{modifier_key}-MINUS"): K("Ctrl-MINUS"),
    K(f"{modifier_key}-EQUAL"): K("Ctrl-Shift-EQUAL"),

    # for tilix
    K(f"{modifier_key}-Key_1"): K("Ctrl-Alt-Key_1"),    # Jump to Tab #1-#8
    K(f"{modifier_key}-Key_2"): K("Ctrl-Alt-Key_2"),
    K(f"{modifier_key}-Key_3"): K("Ctrl-Alt-Key_3"),
    K(f"{modifier_key}-Key_4"): K("Ctrl-Alt-Key_4"),
    K(f"{modifier_key}-Key_5"): K("Ctrl-Alt-Key_5"),
    K(f"{modifier_key}-Key_6"): K("Ctrl-Alt-Key_6"),
    K(f"{modifier_key}-Key_7"): K("Ctrl-Alt-Key_7"),
    K(f"{modifier_key}-Key_8"): K("Ctrl-Alt-Key_8"),
    K(f"{modifier_key}-Key_9"): K("Ctrl-Alt-Key_9"),    # Jump to last tab
}, "terminals")
