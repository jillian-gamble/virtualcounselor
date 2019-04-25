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
		self.counselor.speak("Ok, " + self.client.name + ". Let's start by learning about who you are.")
		self.client.personality = intake.conduct_interview()
		self.counselor.speak("Great, thank you. This will be helpful as I listen to you.")
		self.counselor.speak("Why don't you tell me what's on your mind?")

		while True:
			# Get the user's response and parse it
			response = Statement(input("[YOU]\t\t"), self.client)

			# append it to the conversation
			self.statements.append(response)

			# select a microskill
			self.most_recent_statement().microskill_response = processor.pick_microskill(self)

			# generate it
			processor.test_all_microskills(self)
			#processor.generate_response(self.most_recent_statement().microskill_response, self)


	def most_recent_statement(self):
		return self.statements[len(self.statements) - 1]

class Statement():
	def __init__(self, raw_msg, speaker):
		self.speaker = speaker
		self.raw_msg = raw_msg	# each sentence in the statement
		self.parsed_msg = understander.parse_msg(self)	# parsed_msg is a nlp() object
		self.noun_phrases = [chunk.text for chunk in self.parsed_msg.noun_chunks]
		self.msg_emotions = understander.get_sentence_emotions(self.raw_msg)
		self.msg_topic = understander.get_topic(self.raw_msg, self.parsed_msg)
		self.msg_category = understander.get_category(self.raw_msg, self.parsed_msg)
		self.microskill_response = None

class Client():
	def __init__(self):
		self.name = ""
		self.personality = []	# a dict of trait-->value
		self.mood = {}			# a dict of descriptor-->value

	def is_client(self):
		return True

class Counselor():
	def __init__(self):
		self.persona = []		# the same as client personality
								# except more variable and
								# complementary to the client

	def is_client(self):
		return False

	def speak(self, sentence):
		print("[COUNSELOR]\t" + sentence)

		#tts = gTTS(sentence, lang="en")
		#mixer.init()

		#sf = TemporaryFile()
		#tts.write_to_fp(sf)
		#sf.seek(0)
		#mixer.music.load(sf)
		#mixer.music.play()

		#while mixer.music.get_busy():
		#	pygame.time.wait(100)

	def listen(self):
		print("[YOU]\t\t", end="")

		transcription = input("")# self.get_speech()


		#print(transcription)

		return transcription

	def introduce(self, client):
		self.speak("Hello. Welcome to the Virtual Counselor.")
		self.speak("What's your name?")
		client.name = self.listen()

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
