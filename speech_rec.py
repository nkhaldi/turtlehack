#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json

def distance(a, b):
	n, m = len(a), len(b)
	if n > m:
		a, b = b, a
		n, m = m, n

	current_row = range(n + 1)  # Keep current and previous row, not entire matrix
	for i in range(1, m + 1):
		previous_row, current_row = current_row, [i] + [0] * n
		for j in range(1, n + 1):
			add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
			if a[j - 1] != b[i - 1]:
				change += 1
			current_row[j] = min(add, delete, change)
	return current_row[n]

def runProgramm(text, filename):
	b = [[(0, 171, 125), (255, 255, 186)],
             [(0, 210, 67), (255, 255, 195)],
             [(16, 67, 0), (54, 190, 255)],
             [(162, 123, 0), (255, 255, 255)]]
	a = list()
	a.append(distance(text, "принеси мне синюю губку"))
	a.append(distance(text, "принеси мне зеленую губку"))
	a.append(distance(text, "принеси мне желтую губку"))
	a.append(distance(text, "принеси мне красную губку"))
	m = min(enumerate(a), key=lambda x: x[1])[0]
	json.dump(b[m], open(filename, "w", encoding="utf-8"))
	os.system("cat color.json")
	exit()
"""
#Для установки библиотек:
com_list = []
com_list += ["sudo apt install python3-pip"]
com_list += ["sudo apt-get install portaudio19-dev python-pyaudio python3-pyaudio"]
com_list += ["pip3 install PyAudio"]
com_list += ["pip3 install SpeechRecognition "]
for com in com_list:
	os.system(com)
"""

import speech_recognition as sr

print("Speak!")
while True:
	try:
		record = sr.Recognizer()
		microphone = sr.Microphone()
		with microphone as source:
			record.adjust_for_ambient_noise(source)
			audio = record.listen(source)
			result=record.recognize_google(audio,language="ru_RU")
			result = result.lower()
			runProgramm(format(result), 'color.json')
	except sr.UnknownValueError:
		print('Сервис google не отвечает')
