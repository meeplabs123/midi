import mymidi_global as glo
g = glo.g

import mymidi_utils as Mutils
import mymidi_gui as Mgui

import pygame.midi
import time

def init():
	print("Audio Loading...")
	pygame.midi.init()
	g['in'] = pygame.midi.Input(3)
	g['out'] = pygame.midi.Output(2)
	print_device()
	print("Loaded!")

def print_devices():
	for n in range(pygame.midi.get_count()):
		print(n, pygame.midi.get_device_info(n))

async def read_input(device, last_note):
	if await device.poll():
		event = await device.read(1)[0]

		status = event[0][0]
		timestamp = event[1]

		if last_note == False:
			note = event[0][1]
			velocity = event[0][2]
			channel = event[0][3]
			duration = 0
		else:
			note = last_note[1][0][1]
			velocity = last_note[1][0][2]
			channel = last_note[1][0][3]
			duration = timestamp - last_note[0]

		if (status == 144):
			return [timestamp, event]
		if (channel != 15) & (status == 128):
			return [[status, note, velocity, channel, duration], timestamp, True]
		else:
			return False
	else:
		return False

async def N_single(dev, note, vel, wait):
	Mgui.draw_note_com(note+3)%12, True)
	dev.note_on(note, vel, 15)
	if wait_time == 0:
		time.sleep(vel / 64)
	else:
		time.sleep(wait / 1000)
	dev.note_off(note, 64, 15)
	Mgui.all_notes_off()

async def N_chord(dev, notes, vel, wait):
	for note in notes:
		Mgui.draw_note_com((note+3)%12, True)
		dev.note_on(note, vel, 15)
	if wait_time == 0:
		time.sleep(vel / 64)
	else:
		time.sleep(wait / 1000)
	for note in notes:
		dev.note_off(note, 64, 15)
	Mgui.all_notes_off()	

async def N_arpeg(dev, notes, vel, wait)
	for note in notes:
		Mgui.draw_note_com((note+3)%12, True)
		dev.note_on(note, vel, 15)
		if wait_time == 0:
			time.sleep(vel / 64)
		else:
			time.sleep(wait / 1000)
		dev.note_off(note, 64, 15)
		Mgui.all_notes_off()
