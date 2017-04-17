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

 
preamble = [] # contains headers

dataquest = []	#	Contains ALL data in a list of lists 

instr_cols = [] #	Contains ONLY the instructions in a list of lists




with open(args['file'], 'rb') as csvfile:
	readcsv = csv.reader(csvfile, delimiter = ',')
	for row in readcsv:
		dataquest.append(row)

for i in range(len(dataquest)-12, len(dataquest)):
	instr_cols.append(dataquest[i])
print ">>>>>>>printing instr-cols>>>>>>>>>>>>>>"
print instr_cols
print ">>>>>>>>>>>end>>>>>>>>>>>>>>>>>>>>>>>>>"

preamble = dataquest[0]

def create_dictionary(lolists):
	'''Idea is to create a dictionary that will link a question's ID to
	its attributes.  That is, the key:value pair will be questionID:row
	Map listoflists[i][8] --> listoflists[i]
	'''
	dic = {}
	for i in range(1,len(lolists)-12):			#ignore last 12 cells
		dic[str(lolists[i][8])] = lolists[i]


	#LOGIC FLOW:  there is only one mapping for none,gist,verb
	for j in range(len(lolists)-12, len(lolists)):
		dic[str(lolists[j][8])] = lolists[j]	
 

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
	list_r = ["10", "00"]  				#deleted medium size
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

	if(first_piv == 1):
		first = "gist"
		second = "verb"
	else:
		first = "verb"
		second = "gist"

	out_block.append(first)
	for ele in list_one:
		out_block.append(ele + str(first_piv))
	out_block.append(second)
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
	block_a = shuffle_big_block() #a
	block_b = shuffle_big_block() #b
	block_c = shuffle_big_block() #c
	block_d = shuffle_big_block() #a
	block_e = shuffle_big_block() #b 
	block_f = shuffle_big_block() #c

	out_block = []  #list containing all 108 Q


	# figure out which a,b,c correspond to gist,verb,none
	if(a == "10"):
		a_inst = "gist"
	elif(a == "01"):
		a_inst = "verb"
	else:
		a_inst = "none"

	if(b == "10"):
		b_inst = "gist"
	elif(b == "01"):
		b_inst = "verb"
	else:
		b_inst = "none"

	if(c == "10"):
		c_inst = "gist"
	elif(c == "01"):
		c_inst = "verb"
	else:
		c_inst = "none"	

	print "alsjdflkasdfjalksdjfklajsdlkjfaklsjdfaslkdfj"
	print a_inst
	print b_inst
	print c_inst
	print "ajsdflkajksdjfaklsdjf230903849028309480239492384"
    
    #add instruction
 	#out_block.append(a_inst)


	for ele in block_a:
		if(ele == "gist" or ele  == "verb"):
			out_block.append("p" + a_inst + "" + ele)  #LSB then LSB-1
		else:
			out_block.append(ele + "" + str(a))


	#out_block.append(b_inst)
	#add instruction
	for ele in block_b:
		if(ele == "gist" or ele  == "verb"):
			out_block.append("p" + b_inst + "" + ele)
		else:
			out_block.append(ele + "" + str(b))
	
	

	#out_block.append(c_inst)
	#add instruction
	for ele in block_c:
		if(ele == "gist" or ele  == "verb"):
			out_block.append("p" + c_inst + "" + ele)
		else:
			out_block.append(ele + "" + str(c))


	#out_block.append(a_inst)
	#add instruction
	for ele in block_d:
		if(ele == "gist" or ele  == "verb"):
			out_block.append("w" + a_inst + "" + ele)
		else:
			out_block.append(ele + "" + str(a))

	#out_block.append(b_inst)
	#add instruction
	for ele in block_e:
		if(ele == "gist" or ele  == "verb"):
			out_block.append("w" + b_inst + "" + ele)
		else:
			out_block.append(ele + "" + str(b))	
	
	#out_block.append(c_inst)
	#add instruction
	for ele in block_f:
		if(ele == "gist" or ele  == "verb"):
			out_block.append("w" + c_inst + "" + ele)
		else:
			out_block.append(ele + "" + str(c))

	
	return out_block



def master_shuffle():
	'''merges two 108 quesiton randomized blocks.
	   Outputs twox108 codes in a list.
	   # TODO:  Make instructions a code
	'''
	#determine gist/verbatim/none order
	choices = ["None", "Verbatim", "Gist"]
	pointer_c = ["00", "01", "10"]
	random.shuffle(pointer_c)
	#create shuffle_combine blocks
	shuffled_108_2 = shuffle_combine(pointer_c[0], pointer_c[1], pointer_c[2])
 	foo = []
	foo.extend(shuffled_108_2)

	print "*&&&&&&&&&&&&&showingoutblock&&&&&&&&&&&&&&"
	print foo
	print "2839283892382398283982892329839823182302830"


	return foo



def write_out(dictionary, order):
	
	#print dictionary
	#print order
	outfilename = "thisistheoutputfile" + str(args['seed']) + ".csv"
	with open(outfilename, 'wb') as csvfile:
		outwriter = csv.writer(csvfile, delimiter = ',')
		outwriter.writerow(preamble)
		for value in order:
			print value
			#print dictionary[str(value)]
			outwriter.writerow(dictionary[str(value)])
	return "End of Run."
		

finish = "Program Failure."
order_shuffle =  master_shuffle()
#print order_shuffle
finish = write_out(data_dic, order_shuffle)
print finish




