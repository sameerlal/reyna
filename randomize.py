from math import *
import csv
import argparse



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

x =  dataquest[2]
for i in range(len(x)):
	print x[i]


def create_dictionary(lolists):
	'''Idea is to create a dictionary that will link a question's ID to
	its attributes.  That is, the key:value pair will be questionID:attributes
	'''
	# Use K-th entry to extract the question ID

	#Create an array that stores NEEDED attributes.  Carefuly write this in docs






def parse_file():


	return



def file_reader_crypt():
	# open file

	# parse select data

	# encode

	#return array
	return



def shuffle():
	# shuffle into new array

	# return shuffled array
	return



def write_out():
	# write output file


	return













