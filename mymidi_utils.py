import mymidi_global as glo
g = glo.g

import mymidi_audio as Maudio
import mymidi_gui as Mgui

import os

def init():
	print("Utils Loading...")
	print("Loaded!")

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def get_note(number):
	notes = ['c-', 'c#', 'd-', 'd#', 'e-', 'f-', 'f#', 'g-', 'g#', 'a-', 'a#', 'b-']
	return notes[number%12]
