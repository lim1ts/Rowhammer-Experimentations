#!/usr/bin/env python
import re
import sys

def reverseAddressing(address):
	usefulBits = bitfield(getLast6(address))[::-1]
	ad = []
	ad.append(usefulBits[13]^usefulBits[17])
	ad.append(usefulBits[14]^usefulBits[18])
	ad.append(usefulBits[15]^usefulBits[19])
	ad.append(usefulBits[16]^usefulBits[20])

	return ad

def getLast6(bits):
	return bits[-6:]

def bitfield(bits):
	bitRepresentation = []
	for eachDigit in bits:
		x = int(eachDigit,16)
		for digit in bin(x)[2:].zfill(4):
			if digit == '1':
				bitRepresentation.append(1)
			else:
				bitRepresentation.append(0)
	return bitRepresentation

def sameBanks(a1,a2,v):
	a1Bits = reverseAddressing(a1)
	a2Bits = reverseAddressing(a2)
	vBits = reverseAddressing(v)
	
	return (a1Bits==a2Bits==vBits)

def readLines(myFile):
	totalCount = 0.0
	totalTrue = 0.0
	with open(myFile) as addresses:
		lines = addresses.readlines()
		for eachLine in lines:
			totalCount += 1 
			splitted = eachLine.split(',')
			agg1 = splitted[1]
			agg2 = splitted[2]
			victim = splitted[3]
			print "Checking for", agg1, ",", agg2, " and ", victim
			result = sameBanks(agg1,agg2,victim)
			print result
			if (result):
				totalTrue += 1
		print "--- Finished checks ---"
		print "Number of results tested : ", totalCount
		print "Number of reverse addressing passed : ",  totalTrue
		percentage = totalTrue/totalCount*100
		print "Percentage : ", percentage
	if percentage < 40 :
		"Percentage success too low - check input addresses."

if __name__ == "__main__":
	readLines(sys.argv[1])
