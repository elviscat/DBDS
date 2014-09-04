#!/usr/bin/env python
# -*- coding: utf-8 -*-

# DBDS_Step2.py
# Author: Elvis Hsin-Hui Wu
# Date June 25, 2014
# Calculate the conservative sites and generate non-stationary sites statistical report
# Usage: python DBDS_Step2.py -f folder_name -sl sequence_length -cp consensus_percentage

import os, sys


		
		
def runAnalysis(folderName, maximumLengthOfBasePair, consensusPercentage):
	bpArray = [0] * int(maximumLengthOfBasePair)
	# bpArray = [0 for i in xrange(maximumLengthOfBasePair)]
	# http://stackoverflow.com/questions/1859864/how-to-create-an-integer-array-in-python
	#print bpArray

	# for i in range(2,3):
	#	bpArray[i] = 1
	#	print bpArray

	fileCounter = 0;
	for filename in os.listdir(folderName):
		#print  filename
		#http://stackoverflow.com/questions/120656/directory-listing-in-python
		if "windows.out" in filename:
			#print filename
		
			bpArray2 = [0] * int(maximumLengthOfBasePair)
		
			with open(folderName+'/'+filename) as f:
				content = f.readlines()
				#http://stackoverflow.com/questions/3277503/python-read-file-line-by-line-into-array
				#print content
				#print content[0]
				#print len(content[0].split("\t")[1])
				if len(content[0].split("\t")[1]) > 1:
					for i in content[0].split("\t")[1].split(","):
						lowerBound = int(i.split("-")[0])
						upperBound = int(i.split("-")[1])
						#print str(lowerBound) + '-' + str(upperBound)
						#print str(lowerBound)
						#print '-'
						#print upperBound
					
						adjustedLowerBound = lowerBound-1
						if (lowerBound == 0):
							adjustedLowerBound = 0
						for j in range(adjustedLowerBound, upperBound):
							#if (j == -1):
								#print "j = -1"
								#print lowerBound
								#print lowerBound-1
							#print "j+1"
							#print j
							bpArray[j] +=1
							bpArray2[j] +=1
						
			#print bpArray2
			coverage = 0
			for i in bpArray2:
				if i == 1:
					coverage+=1
			#print "coverage:" + str(coverage)
			print "File: "+ filename + ", Coverage: " + str(float(coverage)/float(len(bpArray2))) + "%"
			#print len(bpArray2)

			if float(coverage)/float(len(bpArray2)) > 0:
					fileCounter+=1



	# if the coverage equals zero, don't include it!!

		
	#print bpArray
	#print bpArray[-1]

	#print "filecounter is ::" + str(fileCounter)
	print "consensus_percentage is :" + str(consensusPercentage) + "%"

	consensus_number = int(int(consensusPercentage) * 0.01 * fileCounter)
	#print "consensus_number is ::" + str(consensus_number)







	# Generate another non-stationary sites statistical report

	# 
	# Union	
	#
	#print bpArray

	print "\n"

	outputStr = ''
	isInRegion = False
	idxCounter = 1
	for i in bpArray:
		#print "bpArray.index(i) = " + str(idxCounter) + "::" + str(i) + "::" + str(isInRegion)
		if i >= 1 and isInRegion == False:
			isInRegion = True
			outputStr += str(idxCounter)
		elif i < 1 and isInRegion == True:
			#print "yes"
			isInRegion = False
			#print isInRegion
			outputStr += "-" + 	str(idxCounter-1) + ","
		idxCounter +=1

	outputStr = outputStr[:-1]		
	print "Union:" + outputStr


	coverage = 0
	for i in bpArray:
		if i >= 1:
			coverage+=1
	#print "coverage:" + str(coverage)
	print "Coverage: " + str(float(coverage)/float(len(bpArray))*100) + "%"


	print "\n"

	outputStr = ''
	isInRegion = False
	idxCounter = 1
	for i in bpArray:
		#print "bpArray.index(i) = " + str(idxCounter) + "::" + str(i) + "::" + str(isInRegion)
		if i >= fileCounter and isInRegion == False:
			isInRegion = True
			outputStr += str(idxCounter)
		elif i < fileCounter and isInRegion == True:
			#print "yes"
			isInRegion = False
			#print isInRegion
			outputStr += "-" + 	str(idxCounter-1) + ","
		idxCounter +=1

	outputStr = outputStr[:-1]		

	print "Intersection:" + outputStr



	coverage = 0
	for i in bpArray:
		if i >= fileCounter:
			coverage+=1
	#print "coverage:" + str(coverage)
	print "Coverage: " + str(float(coverage)/float(len(bpArray))*100) + "%"



	print "\n"



	outputStr = ''
	isInRegion = False
	idxCounter = 1
	for i in bpArray:
		#print "bpArray.index(i) = " + str(idxCounter) + "::" + str(i) + "::" + str(isInRegion)
		if i >= consensus_number and isInRegion == False:
			isInRegion = True
			outputStr += str(idxCounter)
		elif i < consensus_number and isInRegion == True:
			#print "yes"
			isInRegion = False
			#print isInRegion
			outputStr += "-" + 	str(idxCounter-1) + ","
		idxCounter +=1

	outputStr = outputStr[:-1]		

	print "Consensus:" + outputStr

	coverage = 0
	for i in bpArray:
		if i >= consensus_number:
			coverage+=1
	#print "coverage:" + str(coverage)
	print "Coverage: " + str(consensusPercentage) + "%::" +str(float(coverage)/float(len(bpArray))*100) + "%"




if __name__ == "__main__":

	# Usage: python DBDS_Step2.py -f folder_name -sl sequence_length -cp consensus_percentage

	folderName = ''

	maximumLengthOfBasePair = 2000

	consensusPercentage = 0.0

	arguments = sys.argv
	
	argumentsLength = len(arguments)
	
	if argumentsLength == 2 and arguments[1] == '-h':
		print 'Welcome to help!'
		print 'Simple usage of this script: python DBDS_Step2.py -f folder_name -sl sequence_length -cp consensus_percentage'
		print 'For performance concern, the maximum length of sequence is limited to 2000' 
	
	elif argumentsLength == 7:
		for i in range(1, argumentsLength-1):			
			if arguments[i] == '-f' and arguments[i+1] != '' and arguments[i+1] != '-sl' and arguments[i+1] != '-cp':
				folderName = arguments[i+1]			
				if not os.path.exists(folderName):
					print 'Folder doesn\'t exist, please specify the correct folder!'
					exit()
			elif arguments[i] == '-sl' and arguments[i+1] != '' and arguments[i+1] != '-f' and arguments[i+1] != '-cp':
				if int(arguments[i+1]) > 2000:
					print 'For performance concern, the maximum length of sequence is limited to 2000'
					print 'System will use default maximum length of Base Pair => 2000'
				else:
					maximumLengthOfBasePair = arguments[i+1]			

			elif arguments[i] == '-cp' and arguments[i+1] != '' and arguments[i+1] != '-f' and arguments[i+1] != '-sl':
				if int(arguments[i+1]) > 99 or int(arguments[i+1]) < 1:
					print 'The consensus percentage should be between 0 to 100!'
					exit()
				else:
					consensusPercentage = arguments[i+1]	
				

					
			#else:
			#	print 'Wrong parameter setting, please follow the usage: python DBDS_Step2.py -f folder_name -sl sequence_length -cp consensus_percentage'
			#	exit()

		# print folderName
		# print maximumLengthOfBasePair
		# print consensusPercentage
		# BuildBasePairMatrix()
		runAnalysis(folderName, maximumLengthOfBasePair, consensusPercentage)

	else:
		print 'Wrong parameter setting, please follow the usage: python DBDS_Step2.py -f folder_name -sl sequence_length -cp consensus_percentage'
		exit()
