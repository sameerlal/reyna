from math import *
import csv
import argparse
import random



#	Parse Arguments
parser = argparse.ArgumentParser(description='Randomize subject to certain conditions for Hot-Cold study.')
parser.add_argument('-f','--file', help='CSV file containing questions and attributes.  File should be in same directory.', required=True)
parser.add_argument('-s', '--seed', default = "-1", help = 'Participant ID number will be used as a seed for randomization', required = False)
args = vars(parser.parse_args())

 
#print "seed" + args['seed']
#print "file" + args['file']

dataquest = []	#	Contains questions in a list of lists 

with open(args['file'], 'rb') as csvfile:
	readcsv = csv.reader(csvfile, delimiter = ',')
	for row in readcsv:
		dataquest.append(row)
y = dataquest[2]
x =  dataquest[3]
for i in range(len(x)):
	print x[i]
	print y[i]


def create_dictionary(lolists):
	'''Idea is to create a dictionary that will link a question's ID to
	its attributes.  That is, the key:value pair will be questionID:attributes
	'''
	# TODO
	# Use K-th entry to extract the question ID

	#Create an array that stores NEEDED attributes.  Carefuly write this in docs

def master_shuffle():
	'''merges two 108 quesiton randomized blocks.'''





def shuffle_scale_block():
	''''Creates a scale-type-block shuffling category, stim size, plate size
		There are two blocks of this.  18Q
		8-bit:  pqqrrXXX
		p =[0,1] 		 = category
		q = [10,01,00]	 = stimsize
		r = [10,01,11]	 = platesize 

		RETURNS A LIST OF 18 QUESTIONS
	'''
	
	list_q = []
	for i in range(18):
		list_q.append(shuffle_segment())

	return list_q

def shuffle_segment():
	'''Creates one randomized shufled 3-part question
		8-bit:  pqqrrXXX
		p =[0,1] 		 = category
		q = [10,01,00]	 = stimsize
		r = [10,01,11]	 = platesize 
	'''

	#Randomize category
	p = random.choice(['0','1'])
	#Randomize Stimsize
	q = random.choice(['10','01','00'])
	#Randomize Plate Size
	r = random.choice(['10','01','00'])
	
	return p+q+r



def shuffle_combine(a,b,c):
	'''Create 108 randomized 8-bit numbers according to specifications in argument
		Both PM and Wanting will have the same None-Verbatim-Gist (Label type) order
		however within each 18 question block, the questions will be randomized.
	'''
	# SCALE TYPE:  [0 = verbatim, 1= gist]
	# For a, shuffle scale type and make two blocks
	aPivot = random.randint(0,1)
	

	# merge and return
	
	return list_a.append(list_b).append(list_c)

addd = shuffle_combine(1,2,2)
print addd



def write_out():
	# write output file


	return













