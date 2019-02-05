''' This program is responsible for
predicting the best microskill from
the client's speech '''

import app, intake, understander, generator

''' This function predicts which
microskill would be best from the
client's most recent messages'''

def pickMicroskill():
	print("Picking microskill...")