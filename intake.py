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
	print("Please answer the following questions on a scale of 1 to 5")
	personality[O] += input("I am the life of the party.") #openness
	personality[A] += input("I feel little concern for others.") #agreeableness
	personality[C] += input("I am always prepared.") #conscienciousness
	personality[N] += input("I get stressed out easily.") #neuroticism
	personality[O] += input("I have a rich vocabulary.") #openness
	personality[E] += input("I don't talk a lot.") #extroversion
	personality[A] += input("I am interested in people.") #agreeableness
	personality[C] += input("I leave my belongings around.") #conscienciousness
	personality[N] += input("I am relaxed most of the time.") #neuroticism
	personality[O] -= input("I have difficulty understanding abstract ideas.") #openness ANTI??
	personality[E] += input("I feel comfortable around people.") #extroversion
	personality[A] -= input("I insult people.") #agreeableness ANTI??
	personality[C] += input("I pay attention to details.") #conscienciousness
	personality[N] += input("I worry about things.") #neuroticism
	personality[O] += input("I have a vivid imagination.") #openness
	personality[E] += input("I keep in the background.") #extroversion
	personality[A] += input("I sympathize with others' feelings.") #agreeableness
	personality[C] -= input("I make a mess of things.") #conscienciousness ANTI??
	personality[N] -= input("I seldom feel blue.") #neuroticism ANTI??
	personality[O] -= input("I am not interested in abstract ideas.") #openness ANTI??
	personality[E] += input("I start conversations.") #extroversion
	personality[A] += input("I am not interested in other people's problems.") #agreeableness
	personality[C] += input("I get chores done right away.") #conscienciousness
	personality[N] += input("I am easily disturbed.") #neuroticism
	personality[O] += input("I have excellent ideas.") #openness
	personality[E] += input("I have little to say.") #extroversion
	personality[A] += input("I have a soft heart.") #agreeableness
	personality[C] += input("I often forget to put things back in their proper place.") #conscienciousness
	personality[N] += input("I get upset easily.") #neuroticism
	personality[O] += input("I do not have a good imagination.") #openness
	personality[E] += input("I talk to a lot of people at parties.") #extroversion
	personality[E] -= input("I am not really interested in others.") #extroversion ANTI??
	personality[C] += input("I like order.") #conscienciousness
	personality[N] += input("My mood changes a lot.") #neuroticism
	personality[O] += input("I am quick to understand things.") #openness
	personality[E] -= input("I don't like to draw attention to myself.") #extroversion ANTI??
	personality[A] += input("I take time out for others.") #agreeableness
	personality[C] -= input("I shirk my duties.") #conscienciousness ANTI??
	personality[N] += input("I have frequent mood swings.") #neuroticism
	personality[O] += input("I use difficult words.") #openness
	personality[E] += input("I don't mind being the center of attention.")
	personality[A] += input("I feel others' emotions.") #agreeableness
	personality[C] += input("I follow a schedule.") #conscienciousness
	personality[N] += input("I get irritated easily.") #neuroticism
	personality[O] += input("I spend time reflecting on things.") #openness
	personality[E] -= input("I am quiet around strangers.") #extroversion ANTI??
	personality[A] += input("I make people feel at ease.") #agreeableness
	personality[C] += input("I am exacting in my work.") #conscienciousness
	personality[N] += input("I often feel blue.") #neuroticism
	personality[O] += input("I am full of ideas.") #openness

	personality[O] /= 11 # num of openness questions
	personality[C] /= 10 # num of conscienciousness questions
	personality[E] /= 10 # num of extroversion questions
	personality[A] /= 9 # num of agreeableness questions
	personality[N] /= 10 #num of neuroticism questions

	return personality
