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

def conduct_interview():
	personality = [0,0,0,0,0]
	print("Please answer the following questions on a scale of 1 to 5")
	print("")
	personality[O] += int(input("I am the life of the party.\t")) #openness
	personality[A] += int(input("I feel little concern for others.\t")) #agreeableness
	personality[C] += int(input("I am always prepared.\t")) #conscienciousness
	personality[N] += int(input("I get stressed out easily.\t")) #neuroticism
	personality[O] += int(input("I have a rich vocabulary.\t")) #openness
	personality[E] += int(input("I don't talk a lot.\t")) #extroversion
	personality[A] += int(input("I am interested in people.\t")) #agreeableness
	personality[C] += int(input("I leave my belongings around.\t")) #conscienciousness
	personality[N] += int(input("I am relaxed most of the time.\t")) #neuroticism
	personality[O] -= int(input("I have difficulty understanding abstract ideas.\t")) #openness ANTI??
	personality[E] += int(input("I feel comfortable around people.\t")) #extroversion
	personality[A] -= int(input("I insult people.\t")) #agreeableness ANTI??
	personality[C] += int(input("I pay attention to details.\t")) #conscienciousness
	personality[N] += int(input("I worry about things.\t")) #neuroticism
	personality[O] += int(input("I have a vivid imagination.\t")) #openness
	personality[E] += int(input("I keep in the background.\t")) #extroversion
	personality[A] += int(input("I sympathize with others' feelings.\t")) #agreeableness
	personality[C] -= int(input("I make a mess of things.\t")) #conscienciousness ANTI??
	personality[N] -= int(input("I seldom feel blue.\t")) #neuroticism ANTI??
	personality[O] -= int(input("I am not interested in abstract ideas.\t")) #openness ANTI??
	personality[E] += int(input("I start conversations.\t")) #extroversion
	personality[A] += int(input("I am not interested in other people's problems.\t")) #agreeableness
	personality[C] += int(input("I get chores done right away.\t")) #conscienciousness
	personality[N] += int(input("I am easily disturbed.\t")) #neuroticism
	personality[O] += int(input("I have excellent ideas.\t")) #openness
	personality[E] += int(input("I have little to say.\t")) #extroversion
	personality[A] += int(input("I have a soft heart.\t")) #agreeableness
	personality[C] += int(input("I often forget to put things back in their proper place.\t")) #conscienciousness
	personality[N] += int(input("I get upset easily.\t")) #neuroticism
	personality[O] += int(input("I do not have a good imagination.\t")) #openness
	personality[E] += int(input("I talk to a lot of people at parties.\t")) #extroversion
	personality[E] -= int(input("I am not really interested in others.\t")) #extroversion ANTI??
	personality[C] += int(input("I like order.\t")) #conscienciousness
	personality[N] += int(input("My mood changes a lot.\t")) #neuroticism
	personality[O] += int(input("I am quick to understand things.\t")) #openness
	personality[E] -= int(input("I don't like to draw attention to myself.\t")) #extroversion ANTI??
	personality[A] += int(input("I take time out for others.\t")) #agreeableness
	personality[C] -= int(input("I shirk my duties.\t")) #conscienciousness ANTI??
	personality[N] += int(input("I have frequent mood swings.\t")) #neuroticism
	personality[O] += int(input("I use difficult words.\t")) #openness
	personality[E] += int(input("I don't mind being the center of attention.\t"))
	personality[A] += int(input("I feel others' emotions.\t")) #agreeableness
	personality[C] += int(input("I follow a schedule.\t")) #conscienciousness
	personality[N] += int(input("I get irritated easily.\t")) #neuroticism
	personality[O] += int(input("I spend time reflecting on things.\t")) #openness
	personality[E] -= int(input("I am quiet around strangers.\t")) #extroversion ANTI??
	personality[A] += int(input("I make people feel at ease.\t")) #agreeableness
	personality[C] += int(input("I am exacting in my work.\t")) #conscienciousness
	personality[N] += int(input("I often feel blue.\t")) #neuroticism
	personality[O] += int(input("I am full of ideas.\t")) #openness

	personality[O] /= 11 # num of openness questions
	personality[C] /= 10 # num of conscienciousness questions
	personality[E] /= 10 # num of extroversion questions
	personality[A] /= 9 # num of agreeableness questions
	personality[N] /= 10 #num of neuroticism questions

	return personality
