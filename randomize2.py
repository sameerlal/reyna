from math import *
import csv
import argparse
import random
import itertools 



#	Parse Arguments
parser = argparse.ArgumentParser(description='Randomize subject to certain conditions for Hot-Cold study.')
parser.add_argument('-f','--file', help='CSV file containing questions and attributes.  File should be in same directory.', required=True)
parser.add_argument('-s', '--seed', default = "-1", help = 'Participant ID number will be used as a seed for randomization', required = False)
args = vars(parser.parse_args())

 


dataquest = []	#	Contains questions in a list of lists 

with open(args['file'], 'rb') as csvfile:
	readcsv = csv.reader(csvfile, delimiter = ',')
	for row in readcsv:
		dataquest.append(row)

  

def create_dictionary(lolists):
	'''Idea is to create a dictionary that will link a question's ID to
	its attributes.  That is, the key:value pair will be questionID:row
	Map listoflists[i][8] --> listoflists[i]
	'''
	dic = {}
	for i in range(1,len(lolists)):
		dic[str(lolists[i][8])] = lolists[i]
	return dic

# Create mapping
data_dic = create_dictionary(dataquest)
 



def shuffle_small_block():
	''''Creates a scale-type-block shuffling category, stim size, plate size
		There are two blocks of this.  18Q
		8-bit:  pqqrrXXX
		p =[0,1] 		 = category
		q = [10,01,00]	 = stimsize
		r = [10,01,00]	 = platesize 

		RETURNS A LIST OF 18 QUESTIONS
	'''

	out = []

	list_p = ["1", "0"]
	list_q = ["10", "01", "00"]
	list_r = ["10", "01", "00"]
	s = [list_p, list_q, list_r]
	list_pqr = list(itertools.product(*s))
	random.shuffle(list_pqr)
	for item in list_pqr:
		st = ""
		for i in range(3):
			st = st + "" + str(item[i])
		out.append(st)
	return out

def shuffle_big_block():
	'''Creates two blocks of 18Q each, totalling 36 questions.
	Incorporates Scale Type: 0 = Verbatim, 1= gist
	'''
	
	out_block = []
	first_piv = random.randrange(0,2)
	list_one = shuffle_small_block()
	list_two = shuffle_small_block()

	for ele in list_one:
		out_block.append(ele + str(first_piv))
	for ele in list_two:
		out_block.append( ele + str(1-first_piv))
	return out_block #36 Questions




def shuffle_combine(a,b,c):
	'''Create 108 randomized 8-bit numbers according to specifications in argument
		Both PM and Wanting will have the same None-Verbatim-Gist (Label type) order
		however within each 18 question block, the questions will be randomized.
		[10=gist;    01=verb;   00=none]  
		Already in order a,b,c = label type
		Inputs:  a,b,c order of gist/verb/none
		Return:  36*3 = 108 Q

		INcorporates Label type at end
	'''
		# create 3 36-question blocks and postpend a,b,c in that order
	block_a = shuffle_big_block()
	block_b = shuffle_big_block()
	block_c = shuffle_big_block()

	out_block = []  #list containing all 108 Q

	for ele in block_a:
		out_block.append(ele + "" + str(a))
	for ele in block_b:
		out_block.append(ele + "" + str(b))
	for ele in block_c:
		out_block.append(ele + "" + str(c))
	return out_block



def master_shuffle():
	'''merges two 108 quesiton randomized blocks.'''
	#determine gist/verbatim/none order
	choices = ["None", "Verbatim", "Gist"]
	pointer_c = ["00", "01", "10"]
	random.shuffle(pointer_c)
	#create shuffle_combine blocks
	shuffled_108_1 = shuffle_combine(pointer_c[0], pointer_c[1], pointer_c[2])
	shuffled_108_2 = shuffle_combine(pointer_c[0], pointer_c[1], pointer_c[2])
	foo = []
	foo.extend(shuffled_108_1)
	foo.extend(shuffled_108_2)	
	return foo



def write_out(dictionary, order):
	
	#print dictionary
	#print order
	outfilename = "thisistheoutputfile" + str(args['seed']) + ".csv"
	with open(outfilename, 'wb') as csvfile:
		outwriter = csv.writer(csvfile, delimiter = ',')
		for value in order:
			print value
			print dictionary[str(value)]
			outwriter.writerow(dictionary[str(value)])
	return "SUCCESS"
		

finish = "not successful"

order_shuffle =  master_shuffle()
finish = write_out(data_dic, order_shuffle)
print finish




