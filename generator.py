''' This program is responsible for
taking the processor's prediction
and the conversation and outputting
an utterance as response (and
speaking it) '''

import app, intake, understander, processor
import random, string
import bs4 as bs4
import re
import heapq
import nltk

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
			
			nouns.append(noun.capitalize())

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
	statement = conversation.most_recent_statement()

	paraphrase = ""

	for word in statement.raw_msg.split(" "):
		if word == "I" or word == "me":
			paraphrase += " you"

		elif word == "I'm":
			paraphrase += " you're"

		elif word == "I'll":
			paraphrase += " you'll"

		elif word == "I'd":
			paraphrase += " you'd"

		elif word == "I've":
			paraphase += " you've"

		elif word == "my":
			paraphrase += " your"

		elif word == "mine":
			paraphrase += " yours"

		elif word == "am":
			paraphrase += " are"

		elif word == "was":
			paraphrase += " were"

		else:
			paraphrase += " " + word

	conversation.counselor.speak("So, " + paraphrase)
	checkout(conversation)

''' Definition from Ivey et al (2017) p. 135:
"Summarize client comments and integrate throughts, emotions,
and behaviors. Summarizing is similar to paraphrasing but used
over a longer time span."'''
def summarize(conversation):
	print("Summarizing...")
	convo = ""

	for statement in conversation.statements:
		if statement.speaker.is_client():
			convo += statement.raw_msg

	convo = re.sub(r'\[[0-9]*\]', ' ', convo)
	convo = re.sub(r'\s+', ' ', convo)

	formatted_convo = re.sub(r'[^a-zA-Z]', ' ', convo)
	formatted_convo = re.sub(r'\s+', ' ', convo)  

	sentence_list = nltk.sent_tokenize(convo)

	stopwords = nltk.corpus.stopwords.words('english')

	word_frequences = {}

	for word in nltk.word_tokenize(formatted_convo):
		if word not in stopwords:
			if word not in word_frequences.keys():
				word_frequences[word] = 1
			else:
				word_frequences[word] += 1

	maximum_frequency = max(word_frequences.values())

	for word in word_frequences.keys():
		word_frequences[word] = (word_frequences[word]/maximum_frequency)

	sentence_scores = {}

	for sent in sentence_list:
		for word in nltk.word_tokenize(sent.lower()):
			if word in word_frequences.keys():
				if len(sent.split(' ')) < 30:
					if sent not in sentence_scores.keys():
						sentence_scores[sent] = word_frequences[word]
					else:
						sentence_scores[sent] += word_frequences[word]

	summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
	summary = ' '.join(summary_sentences)

	conversation.counselor.speak(summary)

''' Definition from Ivey et al (2017) p. 135:
"Periodically check with your client to discover how your
interviewing lead or skill was received. "Is that right?"
"Did I hear you correctly?" "What might I have missed?""'''
def checkout(conversation):
	print("Checking out...")

	phrases = [
		"Does that sound accurate?",
		"What did I miss?",
		"Right?",
	]

	conversation.counselor.speak(phrases[random.randint(0, len(phrases) - 1)])


def reflect_feelings(conversation):
	print("Reflecting feelings...")

	emotion_options = {
		"FEA":"fear",
		"AMU":"amusement",
		"ANG":"anger",
		"ANN":"annoyance",
		"IDC":"indifference",
		"JOY":"happiness",
		"INS":"inspirational value",
		"SAD":"sadness"
	}

	coded_emotions = understander.get_top_three_emotions(understander.get_sentence_emotions(conversation.most_recent_statement().raw_msg)[1])
	emotions = []

	for cemo in coded_emotions:
		emotions.append(emotion_options[cemo])

	conversation.counselor.speak("I'm sensing some " + emotions[0] + " and also some " + emotions[1] + ".")
	checkout(conversation)

def focus(conversation):
	print("Focusing...")

def reflect_meaning(conversation):
	print("Reflecting meaning...")

def reframe():
	print("Reframing...")
