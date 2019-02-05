''' This program is responsible for 
taking the processor's prediction 
and the conversation and outputting
an utterance as response (and 
speaking it) '''

import app, intake, understander, processor

def question():
	print("Questioning...")

''' Definition from Ivey et al (2017) p. 134:
"Encourage with short responses that help the client keep talking. 
These responses may be verbal (repeating key words and short 
statements) or nonverbal (head-nods and smiling)"'''
def encourage():
	print("Encouraging...")

''' Definition from Ivey et al (2017) p. 134:
"Shorten or clarify the essence of what has just been said, but
be sure to use the client's main words when you paraphrase.
Paraphrases are often fed back to the client in a questioning
tone of voice."'''
def paraphrase():
	print("Paraphrasing...")

''' Definition from Ivey et al (2017) p. 135:
"Summarize client comments and integrate throughts, emotions, 
and behaviors. Summarizing is similar to paraphrasing but used 
over a longer time span."'''
def summarize():
	print("Summarizing...")

''' Definition from Ivey et al (2017) p. 135:
"Periodically check with your client to discover how your 
interviewing lead or skill was received. "Is that right?" 
"Did I hear you correctly?" "What might I have missed?""'''
def checkout():
	print("Checking out...")

def reflect_feelings():
	print("Reflecting feelings...")

def focus():
	print("Focusing...")

def confront():
	print("Confronting...")

def reflect_meaning():
	print("Reflecting meaning...")

def reframe():
	print("Reframing...")