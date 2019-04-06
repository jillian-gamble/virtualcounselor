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
