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
	"CONF",
	"MEAN",
	"REFR"
]					# note: checkout is a microskill used within
					#		paraphrase, summarize, and reflections.
					#		Not by itself. That wouldn't make sense.

''' This function predicts which
microskill would be best from the
client's most recent messages'''
def pick_microskill(conversation):
	ran = random.randint(len(0, MICROSKILLS))

	conversation.most_recent_statement.selected_microskill = ran
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

	elif ms == "CONF":
		generator.confront(conversation)		

	elif ms == "MEAN":
		generator.reflect_meaning(conversation)

	elif ms == "REFR":
		generator.reframe(conversation)

def test_all_microskills(conversation):
	for i in range(len(MICROSKILLS)):
		generate_response(i)

