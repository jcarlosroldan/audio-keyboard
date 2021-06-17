from os import listdir, makedirs
from typing import List
from pynput.keyboard import Listener as KBListener
from simpler import save
from sounddevice import Stream, sleep
import numpy as np

PATH = 'recordings/'

def main(seconds=10, path=PATH) -> None:
	''' Records the default mic sound and the keystroks for the given `seconds`. Then, stores
	it in the path with incremental names. '''
	makedirs(path, exist_ok=True)
	sound, strokes = [], [[0 for _ in range(1, 254)]]

	KBListener(
		on_press=lambda k: track_keyboard(1, k, strokes),
		on_release=lambda k: track_keyboard(-1, k, strokes)
	).start()

	with Stream(callback=lambda data, *others: track_sound(data, sound, strokes)):
		print('recording')
		sleep(1000 * seconds)

	save(path + '%003d.pk' % len(listdir(path)), {'input': np.array(sound), 'output': np.array(strokes)[:-1]})

def track_sound(data: np.ndarray, sound: List[np.ndarray], strokes: List[List[int]]) -> None:
	sound.append(data)
	strokes.append([0 for _ in range(1, 254)])

def track_keyboard(event_type: int, key, strokes: List[List[int]]) -> None:
	key = key.vk if 'vk' in key.__dict__ else key.value.vk
	strokes[-1][key] = event_type

if __name__ == '__main__':
	main()