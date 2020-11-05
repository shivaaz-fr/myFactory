#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
code pour generer un fichier de username base sur une source de type "nom prenom" par ligne

'''
import sys
import argparse

# ------------------------ #
def cmd_line(args):
	parser = argparse.ArgumentParser(description='Generate list of common syntax account name from list')
	parser.add_argument('-o','--outputfile',dest='outputfile',default='stdout', help="file generate with all account names, default stdout")
	requiredNamed = parser.add_argument_group('required named arguments')
	requiredNamed.add_argument('-i','--inputfile',dest='inputfile',default=False, required=True, help="file with each lines like : \"firstname name\"")
	return parser.parse_args()

# ------------------------ #
def generateUsernameList(inArgs,inFile):
	userDict = []
	for line in inFile.readlines():
		(prenom,nom) = line.rstrip().lower().split(" ")
		userDict.append(prenom)
		userDict.append(nom)
		userDict.append(prenom+"."+nom)
		userDict.append(nom+"."+prenom)

		if '-' in prenom :
			(p1,p2) = prenom.split("-")
			userDict.append(p1[0]+p2[0]+"."+nom)		
			userDict.append(p1[0]+p2[0]+nom)
			userDict.append(p1[0]+p2[0]+nom[0])
			userDict.append(p1[0]+p2[0]+nom[0]+nom[1])
			userDict.append(p1[0]+p2[0]+nom[0])
			userDict.append(p1[0]+nom[0]+nom[-1])
			userDict.append(nom+p1[0]+p2[0])
			userDict.append(nom+"."+p1[0]+p2[0])
		else:
			userDict.append(prenom[0]+"."+nom)		
			userDict.append(prenom[0]+nom)
			userDict.append(prenom[0]+nom[0])
			userDict.append(prenom[0]+nom[0]+nom[1])
			userDict.append(prenom[0]+prenom[1]+nom[0])
			userDict.append(prenom[0]+nom[0]+nom[-1])
			userDict.append(nom+prenom[0])
			userDict.append(nom+"."+prenom[0])
	
	if inArgs.outputfile == "stdout":
		for x in userDict:
			print(x)
	else:
		writeOutputfile(inArgs.outputfile,userDict)
	return 0

# ------------------------ #
def writeOutputfile(inOutputfile,inUserDict):
	try:
		with open(inOutputfile,'w') as outputFile:
			for x in inUserDict:
				outputFile.write(x+"\n")
		outputFile.close()
		return(0)
	except Exception as e:
		print("Error: An error accur while opening file: \"{}\" to write in".format(inArgs.inputfile))
		return(3)	

# ------------------------ #
def openFile(inArgs):
	try:
		with open(inArgs.inputfile,'r') as inputFile:
			return generateUsernameList(inArgs,inputFile)
	except FileNotFoundError as e:
		print("Error file not found: \"{}\"".format(inArgs.inputfile))
		return(1)
	except PermissionError as e:
		print("Error permission denied on file: \"{}\"".format(inArgs.inputfile))
		return(2)
	except Exception as e:
		print("Error error while opening file: \"{}\"".format(inArgs.inputfile))
		return(3)

# ------------------------ #
# Start
if __name__ == "__main__":
	args = cmd_line(sys.argv)
	exit(openFile(args))

