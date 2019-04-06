''' This program is responsible for
listening and parsing the client's
speech. '''

import app, intake, processor, generator

CONTENT_AREAS = [
	"STRESS",
	"ANXIETY",
	"DEPRESSION",
	"LOSS",
	"INTERPERSONAL_CONFLICT",
	"INTERNAL_CONFLICT"]	# more ?

MSG_CATEGORIES = [
	"EXPERIENCE",
	"FEELING",
	"MEANING",
	"QUESTION",
	"UNKOWN"]

def parse_msg(msg):
	return msg

def get_emotions(raw_msg, parsed_msg):
	return [0,0,0,0]

def get_topic(raw_msg, parsed_msg):
	return CONTENT_AREAS[0]

def get_category(raw_msg, parsed_msg):
	return MSG_CATEGORIES[0]