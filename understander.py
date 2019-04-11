''' This program is responsible for
listening and parsing the client's
speech. '''

import app, intake, processor, generator
from random import randint
from pickle import load
#from keras.models import load_model
import math
import nltk
import spacy
import numpy as np
import pandas as pd
#from keras.preprocessing.sequence import pad_sequences
#from sklearn.preprocessing import normalize

TOPICS = [
	"STRESS",
	"ANXIETY",
	"DEPRESSION",
	"LOSS",
	"INTERPERSONAL_CONFLICT",
	"INTERNAL_CONFLICT"
	"UNKNOWN"]	# more ?

CATEGORIES = [
	"EXPERIENCE",
	"FEELING",
	"MEANING",
	"QUESTION",
	"UNKOWN"]

nlp = spacy.load("en_core_web_sm")

def parse_msg(msg):
	doc = nlp(msg)
	print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
	return doc

# reduces the class of tags to adj, noun, adv, verb, or UNK
def reduce_tag(tag):
	a = ['JJ', 'JJR', 'JJS', 'PRP$', ]
	n = ['NN', 'NNS', 'NNP', 'NNPS', 'PRP']
	r = ['RB', 'RBR']
	v = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

	if tag in a:
		return 'a'
	if tag in n:
		return 'n'
	if tag in r:
		return 'r'
	if tag in v:
		return 'v'
	else:
		return "UNK"

# stores the 
def load_depeche():
	df = pd.read_csv('DepecheMood_V1.0_all.csv', delimiter=',')
	dicts = [[row[col] for col in df.columns] for row in df.to_dict('records')]

	for entry in dicts:
		#print(entry)
		word = entry[0].split("#")[0]
		pos = entry[0].split("#")[1]

		entry[0] = word
		entry.insert(1, pos)
		entry = [round(entry[i], 3) for i in range(2, 10)]

	return dicts

# pos tag
def tag(token):
	return reduce_tag(nltk.pos_tag([token])[0][1])

# get the emotions for a particular word
def get_lexical_emotions(word, pos = None):
	for entry in EMLEX:
		if entry[0] == word:
			if pos == None or pos == entry[1]:
				return [entry[i] * entry[10] * 10000 for i in range(2,10)]

			else:
				continue
	return [0,0,0,0,0,0,0,0]

def get_stdev(word, pos = None):
	for entry in EMLEX:
		if entry[0] == word:
			if pos == None or pos == entry[1]:
				return entry[10]
			else:
				continue
	return 0

# add a feature for emotions to each word in the line
def get_sentence_emotions(raw_msg):
	words = raw_msg.split(" ")
	tagged_tokens = []

	for word in words:
		word_tag = tag(word)
		tagged_tokens.append(word_tag)		# get the POS -- helps DepecheMood

	if not tagged_tokens:
		return (None, [0,0,0,0,0,0,0,0])

	emo_tokens = []
	line_avg = [0,0,0,0,0,0,0,0]

	for i in range(len(tagged_tokens)):
		tagged_tokens[i] = [words[i], tagged_tokens[i]]

	for token in tagged_tokens:
		emo_features = get_lexical_emotions(token[0], token[1])

		#if emo_features = 

		emo_tokens.append((token[0], token[1], emo_features))

		line_avg = [line_avg[i] + emo_features[i] for i in range(8)]

	line_avg = [round(line_avg[i] / len(tagged_tokens), 2) for i in range(8)]

	return (emo_tokens, line_avg)

def get_topic(raw_msg, parsed_msg):

	return TOPICS[0]

def get_category(raw_msg, parsed_msg):
	return MSG_CATEGORIES[0]

print("Loading DepecheMood...")
EMLEX = load_depeche()
print("Loaded DepecheMood")

emotions = get_sentence_emotions("I am happy")[1]
print("Fear: " + str(emotions[0]))
print("Amusement: " + str(emotions[1]))
print("Anger: " + str(emotions[2]))
print("Annoyance: " + str(emotions[3]))
print("Indifference: " + str(emotions[4]))
print("Happiness: " + str(emotions[5]))
print("Inspiration: " + str(emotions[6]))
print("Sadness: " + str(emotions[7]))