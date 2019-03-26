''' This program is responsible for
collecting personality data in the
initial phase of the program.'''

import app, understander, processor, generator

''' This function will ask a series
of questions to ascertain personality
values '''

O=0
C=1
E=2
A=3
N=4

def ConductInterview():
	personality = [0,0,0,0,0]
	personality[0] += input("I am the life of the party.") #openness
	personality[3] += input("I feel little concern for others.") #agreeableness
	personality[1] += input("I am always prepared.") #conscienciousness
	personality[4] += input("I get stressed out easily.") #neuroticism
	personality[0] += input("I have a rich vocabulary.") #openness
	personality[2] += input("I don't talk a lot.") #extroversion
	personality[3] += input("I am interested in people.") #agreeableness
	personality[1] += input("I leave my belongings around.") #conscienciousness
	personality[4] += input("I am relaxed most of the time.") #neuroticism
	personality[0] -= input("I have difficulty understanding abstract ideas.") #openness ANTI??
	personality[2] += input("I feel comfortable around people.") #extroversion
	personality[3] -= input("I insult people.") #agreeableness ANTI??
	personality[1] += input("I pay attention to details.") #conscienciousness
	personality[4] += input("I worry about things.") #neuroticism
	personality[0] += input("I have a vivid imagination.") #openness
	personality[2] += input("I keep in the background.") #extroversion
	personality[3] += input("I sympathize with others' feelings.") #agreeableness
	personality[1] -= input("I make a mess of things.") #conscienciousness ANTI??
	personality[4] -= input("I seldom feel blue.") #neuroticism ANTI??
	personality[0] -= input("I am not interested in abstract ideas.") #openness ANTI??
	personality[2] += input("I start conversations.") #extroversion
	personality[3] += input("I am not interested in other people's problems.") #agreeableness
	personality[1] += input("I get chores done right away.") #conscienciousness
	personality[4] += input("I am easily disturbed.") #neuroticism
	personality[0] += input("I have excellent ideas.") #openness
	personality[2] += input("I have little to say.") #extroversion
	personality[3] += input("I have a soft heart.") #agreeableness
	personality[1] += input("I often forget to put things back in their proper place.") #conscienciousness
	personality[4] += input("I get upset easily.") #neuroticism
	personality[0] += input("I do not have a good imagination.") #openness
	personality[2] += input("I talk to a lot of people at parties.") #extroversion
	personality[2] -= input("I am not really interested in others.") #extroversion ANTI??
	personality[1] += input("I like order.") #conscienciousness
	personality[4] += input("My mood changes a lot.") #neuroticism
	personality[0] += input("I am quick to understand things.") #openness
	personality[2] -= input("I don't like to draw attention to myself.") #extroversion ANTI??
	personality[3] += input("I take time out for others.") #agreeableness
	personality[1] -= input("I shirk my duties.") #conscienciousness ANTI??
	personality[4] += input("I have frequent mood swings.") #neuroticism
	personality[0] += input("I use difficult words.") #openness
	personality[2] += input("I don't mind being the center of attention.")
	personality[3] += input("I feel others' emotions.") #agreeableness
	personality[1] += input("I follow a schedule.") #conscienciousness
	personality[4] += input("I get irritated easily.") #neuroticism
	personality[0] += input("I spend time reflecting on things.") #openness
	personality[2] -= input("I am quiet around strangers.") #extroversion ANTI??
	personality[3] += input("I make people feel at ease.") #agreeableness
	personality[1] += input("I am exacting in my work.") #conscienciousness
	personality[4] += input("I often feel blue.") #neuroticism
	personality[0] += input("I am full of ideas.") #openness

	personality[O] /= 11 # num of openness questions
	personality[1] /= 10 # num of conscienciousness questions
	personality[2] /= 10 # num of extroversion questions
	personality[3] /= 9 # num of agreeableness questions
	personality[4] /= 10 #num of neuroticism questions

	return personality
