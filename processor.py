''' This program is responsible for
predicting the best microskill from
the client's speech '''

import app, intake, understander, generator
import random

MICROSKILLS = [
	"QUES",
	"ENCO",
	"PARA",
	"SUMM",
	"FEEL",
	"FOCU",
	"MEAN",
	"REFR"
]					# note: checkout is a microskill used within
					#		paraphrase, summarize, and reflections.
					#		Not by itself. That wouldn't make sense.

''' This function predicts which
microskill would be best from the
client's most recent messages'''
def pick_microskill(conversation):
	ran = random.randint(0, len(MICROSKILLS) - 1)

	conversation.most_recent_statement().selected_microskill = ran
	return ran

def generate_response(nMicroskill, conversation):
	ms = MICROSKILLS[nMicroskill]

	if ms == "QUES":
		generator.question(conversation)

	elif ms == "ENCO":
		generator.encourage(conversation)

	elif ms == "PARA":
		generator.paraphrase(conversation)

	elif ms == "SUMM":
		generator.summarize(conversation)

	elif ms == "FEEL":
		generator.reflect_feelings(conversation)

	elif ms == "FOCU":
		generator.focus(conversation)		

	elif ms == "MEAN":
		generator.reflect_meaning(conversation)

	elif ms == "REFR":
		generator.reframe(conversation)

def test_all_microskills(conversation):
	for i in range(0, len(MICROSKILLS) - 1):
		generate_response(i, conversation)

