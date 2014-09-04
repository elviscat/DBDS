#!/usr/bin/env python
# -*- coding: utf-8 -*-

# DBDS_Step1.py
# Author: Elvis Hsin-Hui Wu
# Date June 25, 2014
# Batch execute pyDruids.py and store analysis results in designated folder
# Usage: python DBDS_Step1.py -s example.nex

from Bio.Nexus import Nexus
from Bio import SeqIO
import os, sys


def delFolderContent(folder):
	for the_file in os.listdir(folder):
		file_path = os.path.join(folder, the_file)
		try:
			if os.path.isfile(file_path):
				os.unlink(file_path)
		except Exception, e:
			print e


def readNexFile(fileName):
	seq = {}
	if fileName != '':
		# read data set file, requires biopython
		handle = open(fileName, 'r')
		if fileName.endswith('nex') or fileName.endswith('nexus'):
			seq = SeqIO.to_dict(SeqIO.parse(handle, 'nexus'))
		elif fileName.endswith('phy') or fileName.endswith('phylip'):
			seq = SeqIO.to_dict(SeqIO.parse(handle, 'phylip'))
		elif fileName.endswith('fasta'):
			seq = SeqIO.to_dict(SeqIO.parse(handle, 'fasta'))
		handle.close()
	return seq		


def DruidsWrapper(fileName, outputFolderName, seq):

	nchar = len(seq[seq.keys()[0]])
	ntaxa = len(seq.keys())
	print 'nchar:' + str(nchar)
	print 'ntaxa:' + str(ntaxa)
	
	# windowSize = min(windowSize,nchar/2) # limit windosize to thalf the data set length

	# model_array = ["V", "H", "C", "V,H", "V,C", "H,C", "V,H,C"] # w/ combine model
	model_array = ["V", "H", "C", "GC"]

	
	for i in range(3,(nchar/2),3):
	# for i in range(3,45,3): # Just for testing
		#print i
		for j in model_array:
			# example
			# os.system("python pyDruids.py -f " + fileName + " -w 24 -a V_H_C -o 111/test_window_24_V_H_C")
			# os.system("python pyDruids.py -f " + fileName + " -w 21 -a V_H_C -o 111/test_window_21_V_H_C")
			
			command = "python pyDruids.py -f " + fileName + " -w " + str(i) + " -a " + j + " -o " + outputFolderName + "/" + outputFolderName + "_test_window_"+ str(i) + "_" + j 	
			# print command
			os.system(command)



if __name__ == "__main__":

	# Usage: python DBDS_Step1.py -s example.nex
	
	fileName = ''
	outputFolderName = ''
	
	arguments = sys.argv
	
	argumentsLength = len(arguments)
	
	if argumentsLength == 2 and arguments[1] == '-h':
		print 'Welcome to help!'
		print 'Simple usage of this script: python DBDS_Step1.py -s example.nex'
	
	elif argumentsLength == 3:
		for i in range(1, argumentsLength-1):			
			if arguments[i] == '-s' and arguments[i+1] != '' and arguments[i+1] != '-s':
				fileName = arguments[i+1]
				outputFolderName = fileName.split(".")[0]
			
				if not os.path.exists(outputFolderName):
					os.mkdir(outputFolderName)
				else:
					delFolderContent(outputFolderName)
					
				if len(readNexFile(fileName)) > 0:
					# print len(readNexFile(fileName))
					print 'Load sequence file ...'
					seq = readNexFile(fileName)
					DruidsWrapper(fileName, outputFolderName, seq)
					
				else:
					print 'Can\'t load the sequence, probably wrong format. Support format: nexus, phylip, fasta.'
					
			else:
				print 'Wrong parameter setting, please follow the usage: python DBDS_Step1.py -s example.nex'		
	else:
		print 'Wrong parameter setting, please follow the usage: python DBDS_Step1.py -s example.nex'

