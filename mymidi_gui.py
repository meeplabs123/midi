import mymidi_global as glo
g = glo.g

import mymidi_utils as Mutils
import mymidi_audio as Maudio

import curses
import time
import asyncio

def init():
	print("GUI Loading...")
	curses.wrapper(main)
	print("Loaded!")

def main(stdscr):
	stdscr.clear()
	g['stdscr'] = stdscr
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
	curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
	curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)
	
	g['COL'] = []
	for n in range(100):
		g['COL'].append(0)
	
	for v in range(6):
		i = v+1
		g['COL'][i] = curses.color_pair(v)
	for v in range(6):
		i = v+7
		g['COL'][i] = curses.color_pair(v) | curses.A_BOLD
	for v in range(6):
		i = v+13
		g['COL'][i] = curses.color_pair(v) | curses.A_DIM
	for v in range(6):
		i = v+19
		g['COL'][i] = curses.color_pair(v) | curses.A_BLINK
	for v in range(6):
		i = v+25
		g['COL'][i] = curses.color_pair(v) | curses.A_BOLD | curses.A_BLINK
	for v in range(6):
		i = v+31
		g['COL'][i] = curses.color_pair(v) | curses.A_BOLD | curses.A_DIM

async def print_test():
	for i in range(36):
		num = str(i+1)
		if len(num) == 1:
			num = "00" + num
		elif len(num) == 2:
			num = "0" + num

		g['stdscr'].addstr(i+2,0, "[" + num + "] Fancy Text!", g['COL'][i+1])
		g['stdscr'].refresh()

	while True:
		g['stdscr'].addstr(0, 0, "[:] Waiting...  ", g['COL'][7])
		g['stdscr'].refresh()
		await asyncio.sleep(1)

		g['stdscr'].addstr(0, 0, "[.] Waiting...  ", g['COL'][8])
		g['stdscr'].refresh()
		await asyncio.sleep(1)

		g['stdscr'].addstr(0, 0, "[!] Error!  ", g['COL'][9])
		g['stdscr'].refresh()
		await asyncio.sleep(1)

		g['stdscr'].addstr(0, 0, "[#] Playing...  ", g['COL'][10])
		g['stdscr'].refresh()
		await asyncio.sleep(1)

		g['stdscr'].addstr(0, 0, "[%] Recording...", g['COL'][11])
		g['stdscr'].refresh()
		await asyncio.sleep(1)

		g['stdscr'].addstr(0, 0, "[~] Loading...  ", g['COL'][12])
		g['stdscr'].refresh()
		await asyncio.sleep(1)

async def print_program():
	all_notes_off()

	g['stdscr'].addstr(0, 0, "[:] Waiting...  ", g['COL'][7])
	g['stdscr'].refresh()

	last = False

	while True:
		input = await Maudio.read_input(my_device_in, last)
		if isinstance(input, list):
			if len(input) == 2:
				# NOTE STARTED
				last = input
				draw_note((input[1][0][1]+3)%12, True)
				g['stdscr'].refresh()
			elif len(input) > 2:
				# NOTE FINISHED
				status = input[0][0]
				timestamp = input[1]
				note = input[0][1]
				velocity = input[0][2]
				channel = input[0][3]
				duration = input[0][4]

				draw_note((input[0][1]+3)%12, False)

				all_notes_off()
				
				g['stdscr'].addstr(12, 0, "| Note: " + Mutils.get_note(note) + " [" + str(note) + "[ | Velocity: " + str(velocity) + " | Channel: " + str(channel0 + " | Duration: " + str(duration) + " |          ", g['COL'][8])
				g['stdscr'].refresh()
				N_single(g['out'], note, velocity, duration)

async def all_notes_off():
	for i in range(20):
		draw_note(i, False)

async def draw_note(note, state):
	if state:
		targetcolor = g['COL'][1]
	else:
		targetcolor = g['COL'][2]
	
	if note == 0:
		g['stdscr'].addstr(2, 0, "/----\\", targetcolor)
		g['stdscr'].addstr(3, 0, "| a- |", targetcolor)
		g['stdscr'].addstr(4, 0, "\----/", targetcolor)
	if note == 1:
		g['stdscr'].addstr(3, 7, "/----\\", targetcolor)
		g['stdscr'].addstr(4, 7, "| a# |", targetcolor)
		g['stdscr'].addstr(5, 7, "\----/", targetcolor)
	if note == 2:
		g['stdscr'].addstr(2, 14, "/----\\", targetcolor)
		g['stdscr'].addstr(3, 14, "| b- |", targetcolor)
		g['stdscr'].addstr(4, 14, "\----/", targetcolor)
	if note == 3:
		g['stdscr'].addstr(3, 21, "/----\\", targetcolor)
		g['stdscr'].addstr(4, 21, "| c- |", targetcolor)
		g['stdscr'].addstr(5, 21, "\----/", targetcolor)
	if note == 4:
		g['stdscr'].addstr(2, 28, "/----\\", targetcolor)
		g['stdscr'].addstr(3, 28, "| c# |", targetcolor)
		g['stdscr'].addstr(4, 28, "\----/", targetcolor)
	if note == 5:
		g['stdscr'].addstr(3, 35, "/----\\", targetcolor)
		g['stdscr'].addstr(4, 35, "| d- |", targetcolor)
		g['stdscr'].addstr(5, 35, "\----/", targetcolor)
	if note == 6:
		g['stdscr'].addstr(7, 0, "/----\\", targetcolor)
		g['stdscr'].addstr(8, 0, "| d# |", targetcolor)
		g['stdscr'].addstr(9, 0, "\----/", targetcolor)
	if note == 7:
		g['stdscr'].addstr(8, 7, "/----\\", targetcolor)
		g['stdscr'].addstr(9, 7, "| e- |", targetcolor)
		g['stdscr'].addstr(10, 7, "\----/", targetcolor)
	if note == 8:
		g['stdscr'].addstr(7, 14, "/----\\", targetcolor)
		g['stdscr'].addstr(8, 14, "| f- |", targetcolor)
		g['stdscr'].addstr(9, 14, "\----/", targetcolor)
	if note == 9:
		g['stdscr'].addstr(8, 21, "/----\\", targetcolor)
		g['stdscr'].addstr(9, 21, "| f# |", targetcolor)
		g['stdscr'].addstr(10, 21, "\----/", targetcolor)
	if note == 10:
		g['stdscr'].addstr(7, 28, "/----\\", targetcolor)
		g['stdscr'].addstr(8, 28, "| g- |", targetcolor)
		g['stdscr'].addstr(9, 28, "\----/", targetcolor)
	if note == 11:
		g['stdscr'].addstr(8, 35, "/----\\", targetcolor)
		g['stdscr'].addstr(9, 35, "| g# |", targetcolor)
		g['stdscr'].addstr(10, 35, "\----/", targetcolor)

async def draw_note_com(note, state):
	if state:
		targetcolor = g['COL'][4]
	else:
		targetcolor = g['COL'][2]
	
	if note == 0:
		g['stdscr'].addstr(2, 0, "/----\\", targetcolor)
		g['stdscr'].addstr(3, 0, "| a- |", targetcolor)
		g['stdscr'].addstr(4, 0, "\----/", targetcolor)
	if note == 1:
		g['stdscr'].addstr(3, 7, "/----\\", targetcolor)
		g['stdscr'].addstr(4, 7, "| a# |", targetcolor)
		g['stdscr'].addstr(5, 7, "\----/", targetcolor)
	if note == 2:
		g['stdscr'].addstr(2, 14, "/----\\", targetcolor)
		g['stdscr'].addstr(3, 14, "| b- |", targetcolor)
		g['stdscr'].addstr(4, 14, "\----/", targetcolor)
	if note == 3:
		g['stdscr'].addstr(3, 21, "/----\\", targetcolor)
		g['stdscr'].addstr(4, 21, "| c- |", targetcolor)
		g['stdscr'].addstr(5, 21, "\----/", targetcolor)
	if note == 4:
		g['stdscr'].addstr(2, 28, "/----\\", targetcolor)
		g['stdscr'].addstr(3, 28, "| c# |", targetcolor)
		g['stdscr'].addstr(4, 28, "\----/", targetcolor)
	if note == 5:
		g['stdscr'].addstr(3, 35, "/----\\", targetcolor)
		g['stdscr'].addstr(4, 35, "| d- |", targetcolor)
		g['stdscr'].addstr(5, 35, "\----/", targetcolor)
	if note == 6:
		g['stdscr'].addstr(7, 0, "/----\\", targetcolor)
		g['stdscr'].addstr(8, 0, "| d# |", targetcolor)
		g['stdscr'].addstr(9, 0, "\----/", targetcolor)
	if note == 7:
		g['stdscr'].addstr(8, 7, "/----\\", targetcolor)
		g['stdscr'].addstr(9, 7, "| e- |", targetcolor)
		g['stdscr'].addstr(10, 7, "\----/", targetcolor)
	if note == 8:
		g['stdscr'].addstr(7, 14, "/----\\", targetcolor)
		g['stdscr'].addstr(8, 14, "| f- |", targetcolor)
		g['stdscr'].addstr(9, 14, "\----/", targetcolor)
	if note == 9:
		g['stdscr'].addstr(8, 21, "/----\\", targetcolor)
		g['stdscr'].addstr(9, 21, "| f# |", targetcolor)
		g['stdscr'].addstr(10, 21, "\----/", targetcolor)
	if note == 10:
		g['stdscr'].addstr(7, 28, "/----\\", targetcolor)
		g['stdscr'].addstr(8, 28, "| g- |", targetcolor)
		g['stdscr'].addstr(9, 28, "\----/", targetcolor)
	if note == 11:
		g['stdscr'].addstr(8, 35, "/----\\", targetcolor)
		g['stdscr'].addstr(9, 35, "| g# |", targetcolor)
		g['stdscr'].addstr(10, 35, "\----/", targetcolor)

async def get_text(callback):
	g['stdscr'].addstr(13, 0, "==============================", g['COL'][1])
	g['stdscr'].addstr(14, 0, "|                            |", g['COL'][1])
	g['stdscr'].addstr(15, 0, "==============================", g['COL'][1])
	text = g['stdscr'].getkey(14, 2)
	return text
