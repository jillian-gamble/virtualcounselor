''' This program is responsible for
listening and parsing the client's
speech. '''
print("Loading imports...")

import app, intake, processor, generator
from random import randint
from pickle import load
#from keras.models import load_model
import math
import nltk
import spacy
import numpy as np
import pandas as pd
from nltk.corpus import wordnet as wn

print("Loaded imports")
#from keras.preprocessing.sequence import pad_sequences
#from sklearn.preprocessing import normalize

TOPICS = {
	"STRESS":0,
	"ANXIETY":1,
	"DEPRESSION":2,
	"LOSS":3,
	"INTERPERSONAL_CONFLICT":4,
	"INTERNAL_CONFLICT":5,
	"UNKNOWN":6}	# more ?

CATEGORIES = {
	"EXPERIENCE":1,
	"FEELING":2,
	"MEANING":3,
	"QUESTION":4,
	"UNKNOWN":5}

EMOTION_WORDS = wn.synsets("feeling")[0].hyponyms()
EMOTION_WORDS.extend(wn.synsets("emotion")[0].hyponyms())

#print(EMOTION_WORDS)

nlp = spacy.load("en_core_web_sm")

def parse_msg(statement):
	doc = nlp(statement.raw_msg)
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
		return "UNK"L

# pos tag
def tag(token):
	return reduce_tag(nltk.pos_tag([token])[0][1])

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

def is_lemma(word, synset):
	return word in synset.lemma_names()

def is_emotion_word(word):
	for synset in EMOTION_WORDS:
		if is_lemma(word, synset):
			return True

	return False

def get_emotionality(word, pos = None):
	if is_emotion_word(word):
		return 10

	return math.floor(26.2292*get_stdev(word, pos) + 0.11259)

# get the emotions for a particular word
def get_lexical_emotions(word, pos = None):
	for entry in EMLEX:
		if entry[0] == word:
			if pos == None or pos == entry[1]:
				#print(entry)
				return [math.pow(entry[i], entry[10]) * get_emotionality(word, pos) for i in range(2,10)]

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

	# divide the total intensity by the total number of words for each emotion
	line_avg = [round(line_avg[i] / len(tagged_tokens), 2) for i in range(8)]

	return (emo_tokens, line_avg)

def get_topic(raw_msg, parsed_msg):

	return TOPICS["UNKNOWN"]

# this function classifies the statement as experience, feeling/emotion,
# meaning, question, or other
def get_category(raw_msg, parsed_msg):
	#exp_freq = 

	return CATEGORIES["UNKNOWN"]

def get_top_three_emotions(arr):
	max_i = -1
	max_val = -1

	result = []

	emotions = ["FEA", "AMU", "ANG", "ANN", "IDC", "JOY", "INS", "SAD"]

	for j in range(3):
		for i in range(len(arr)):

			if arr[i] > max_val:
				max_val = arr[i]
				max_i = i

		result.append(emotions[max_i])

		arr.pop(max_i)
		emotions.pop(max_i)

		max_i = -1
		max_val = -1

	return result

print("Loading DepecheMood...")
EMLEX = load_depeche()
print("Loaded DepecheMood")

	# while 1:
	# 	# emotions = get_sentence_emotions(input("Sentence: "))[1]
	# 	# print("\nFear: " + str(emotions[0]))
	# 	# print("Amusement: " + str(emotions[1]))
	# 	# print("Anger: " + str(emotions[2]))
	# 	# print("Annoyance: " + str(emotions[3]))
	# 	# print("Indifference: " + str(emotions[4]))
	# 	# print("Happiness: " + str(emotions[5]))
	# 	# print("Inspiration: " + str(emotions[6]))
	# 	# print("Sadness: " + str(emotions[7]) + "\n")
	# 	# print("Top 3 Emotions: " + str(get_top_three_emotions(emotions)))
	# 	word = input("Word: ")
	# 	print(is_emotion_word(word))
	# 	print(get_emotionality(word))
	# 	print(get_top_three_emotions(get_lexical_emotions(word)))