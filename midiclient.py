import time
import curses
import asyncio
import pygame.midi

import mymidi_global as glo
g = glo.g

import mymidi_utils as Mutils
import mymidi_audio as Maudio
import mymidi_gui as Mgui

Mutils.init()
Maudio.init()
Mgui.init()

Mutils.clear()
