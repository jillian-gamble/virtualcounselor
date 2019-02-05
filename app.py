''' This program is responsible for 
instantiating the GUI, connecting
to the microphone and speaker, and
managing the program flow '''

import intake, understander, processor, generator
import os

# tts
from gtts import gTTS
from io import BytesIO
import pygame
from pygame import mixer
from tempfile import TemporaryFile

# stt
import speech_recognition as sr

UNK = -1
COUNSELOR = 0
CLIENT = 1

class App():
	def __init__(self):
		# First, instantiate all the relevant objects
		self.client = Client()
		self.counselor = Counselor()
		self.conversation = Conversation(self.counselor, self.client)

class Conversation():
	def __init__(self, counselor, client):
		self.statements = []	# a list of statements
		self.counselor = counselor
		self.client = client

	def start(self):
		self.counselor.introduce(self.client)


class Statement():
	def __init__(self, statement, speaker):
		self.speaker = speaker
		self.statement = statement	# each sentence in the statement

	def process_syntax(self):
		words = statement.split(" ")

class Client():
	def __init__(self):
		self.name = ""
		self.personality = {}	# a dict of trait-->value
		self.mood = {}			# a dict of descriptor-->value

class Counselor():
	def __init__(self):
		self.persona = []		# the same as client personality 
								# except more variable and 
								# complementary to the client

	def speak(self, sentence):
		print("COUNSELOR: " + sentence)

		tts = gTTS(sentence, lang="en")
		mixer.init()

		sf = TemporaryFile()
		tts.write_to_fp(sf)
		sf.seek(0)
		mixer.music.load(sf)
		mixer.music.play()

		while mixer.music.get_busy():
			pygame.time.wait(100)
		
	def listen(self):
		print("YOU: ", end="")

		transcription = self.get_speech()

		print(transcription)

		return transcription

	def introduce(self, client):
		self.speak("Hello. Welcome to the Virtual Counselor.")
		self.speak("What's your name?")
		client.name = self.listen()
		self.speak("Ok, " + client.name + ". Let's start by learning about who you are.")

	def get_speech(self):
		r = sr.Recognizer()
		mic = sr.Microphone()

		with mic as source:
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)

		return(r.recognize_google(audio))

if __name__ == "__main__":
	app = App()					# instantiate the app, client, counselor, and convo

	app.conversation.start()	# start the conversation
