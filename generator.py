''' This program is responsible for
taking the processor's prediction
and the conversation and outputting
an utterance as response (and
speaking it) '''

import app, intake, understander, processor
import random, string

def question(conversation):
	print("Questioning...")

''' Definition from Ivey et al (2017) p. 134:
"Encourage with short responses that help the client keep talking.
These responses may be verbal (repeating key words and short
statements) or nonverbal (head-nods and smiling)"'''
def encourage(conversation):
	print("Encouraging...")

	candidate_nouns = conversation.most_recent_statement().noun_phrases

	nouns = []
	for noun in candidate_nouns:
		if len(noun.split(" ")) > 1:
			noun[0] = noun[0].upper()
			nouns.append(noun)

	phrases = [
		"Interesting. Tell me more.",
		"Okay, I'm listening.",
		(nouns[random.randint(0, len(nouns) - 1)] if len(nouns) > 0 else "Alright") + ". Okay.",
		"Yes, okay.",
		"Mmmmm, I see.",
		"Of course."
	]

	conversation.counselor.speak(phrases[random.randint(0, len(phrases) - 1)])

''' Definition from Ivey et al (2017) p. 134:
"Shorten or clarify the essence of what has just been said, but
be sure to use the client's main words when you paraphrase.
Paraphrases are often fed back to the client in a questioning
tone of voice."'''
def paraphrase(conversation):
	print("Paraphrasing...")

''' Definition from Ivey et al (2017) p. 135:
"Summarize client comments and integrate throughts, emotions,
and behaviors. Summarizing is similar to paraphrasing but used
over a longer time span."'''
def summarize(conversation):
	print("Summarizing...")

''' Definition from Ivey et al (2017) p. 135:
"Periodically check with your client to discover how your
interviewing lead or skill was received. "Is that right?"
"Did I hear you correctly?" "What might I have missed?""'''
def checkout(conversation):
	print("Checking out...")


def reflect_feelings(conversation):
	print("Reflecting feelings...")

def focus(conversation):
	print("Focusing...")

def reflect_meaning(conversation):
	print("Reflecting meaning...")

def reframe():
	print("Reframing...")
