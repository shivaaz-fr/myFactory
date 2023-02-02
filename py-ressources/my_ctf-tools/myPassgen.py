#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ouverture d'un fichier avec les mots a manipuler
dans le fichier : un mot par ligne

mot de passe type:
astrel <= base
asTrel <= 1 cap / a mettre sur chaque lettre
AstreL <= 2 cap / 1 debut + 1 fin
@strel <= 1 subs
@str3l <= 2 subs
@streL <= 1 cap debut ou fin + 1subs

pour chaque possibilite :
-> on met un @ au debut
-> on met un ! a la fin
-> mettre 1 jusqu a 4 chiffres a la fin
-> mettre @  et mettre 2 jusqu a 4 chiffres
-> mettre !  et mettre 2 jusqu a 4 chiffres
-> mettre -  et mettre 2 jusqu a 4 chiffres
-> mettre _  et mettre 2 jusqu a 4 chiffres
-> mettre %  et mettre 2 jusqu a 4 chiffres
-> mettre $  et mettre 2 jusqu a 4 chiffres

si plusieurs mot par ligne :
-> nom1!nom2
-> nom2!nom1
-> nom1&nom2
-> nom2&nom1
-> nom1@nom2
-> nom2@nom1
-> nom1-nom2
-> nom2-nom1
...

type d'actions :

'''

# utilisation de la lib itertools et de la methode product()
# https://docs.python.org/fr/3/library/itertools.html
from itertools import product
import sys
import argparse

# ------------------------ #
#dictionary containing all substitutions
subDictFULL = {
	'a': ['a','A','@','4'],
	'b': ['b','B','8','6'],
	'c': ['c','C','[','{','(','<'], 
	'd': ['d','D',], 
	'e': ['e','E','3'], 
	'f': ['f','F'], 
	'g': ['g','G','6','9'], 
	'h': ['h','H','#'], 
	'i': ['i','I','1','l','L','|','!'], 
	'j': ['j','J'], 
	'k': ['k','K'], 
	'l': ['l','L','i','I','|','!','1'], 
	'm': ['m','M'], 
	'n': ['n','N'], 
	'o': ['o','O','0','Q'], 
	'p': ['p','P'], 
	'q': ['q','Q','9','0','O'], 
	'r': ['r','R'], 
	's': ['s','S','$','5'], 
	't': ['t','T','+','7'], 
	'u': ['u','U','v','V'], 
	'v': ['v','V','u','U'], 
	'w': ['w','W'], 
	'x': ['x','X','+'], 
	'y': ['y','Y'], 
	'z': ['z','Z','2'], 
}

# #dictionary containing substitutions
subDictLIGHT = {
	'a': ['a','A','@'],
	'b': ['b','B'],
	'c': ['c','C'], 
	'd': ['d','D'], 
	'e': ['e','E','3'], 
	'f': ['f','F'], 
	'g': ['g','G'], 
	'h': ['h','H'], 
	'i': ['i','I','1'], 
	'j': ['j','J'], 
	'k': ['k','K'], 
	'l': ['l','L','I','1'], 
	'm': ['m','M'], 
	'n': ['n','N'], 
	'o': ['o','O','0'], 
	'p': ['p','P'], 
	'q': ['q','Q'], 
	'r': ['r','R'], 
	's': ['s','S','$'], 
	't': ['t','T','7'], 
	'u': ['u','U'], 
	'v': ['v','V'], 
	'w': ['w','W'], 
	'x': ['x','X'], 
	'y': ['y','Y'], 
	'z': ['z','Z'], 
}

#special characters commonly appended to passwords to meet complexity requirements
specChar = ['!','@','$','%','&','*','?','-','_']

#used to generate 4 digit number to append to passwords
numbersOnly = ['1','2','3','4','5','6','7','8','9','0']

# ------------------------ #
# Fonction pour faire la substitution des chars
def doSubstitution(fd):
	'''
	https://www.hackerrank.com/challenges/itertools-product/problem
	https://www.tutorialspoint.com/python3/string_join.htm
	https://docs.python.org/fr/3/library/itertools.html
	chaque lettre est recherche dans les clés du dictio
	s'il y a une clé qui existe, on rajoute la valeur (les subs) à une liste
	a la fin on option une liste avec pour chaque lettre les possibilités
	il suffit de faire appel a à la fonction itertool.product() qui
	fait un produit caterisien de toutes les possiblites

	exemple pour le mot "briche"
	briche
	b
	la liste vaut maintenant :  [['b', 'B', '8', '6']]
	r
	la liste vaut maintenant :  [['b', 'B', '8', '6'], ['r', 'R']]
	i
	la liste vaut maintenant :  [['b', 'B', '8', '6'], ['r', 'R'], ['i', 'I', '1', 'l', 'L', '|', '!']]
	c
	la liste vaut maintenant :  [['b', 'B', '8', '6'], ['r', 'R'], ['i', 'I', '1', 'l', 'L', '|', '!'], ['c', 'C', '[', '{', '(', '<']]
	h
	la liste vaut maintenant :  [['b', 'B', '8', '6'], ['r', 'R'], ['i', 'I', '1', 'l', 'L', '|', '!'], ['c', 'C', '[', '{', '(', '<'], ['h', 'H', '#']]
	e
	la liste vaut maintenant :  [['b', 'B', '8', '6'], ['r', 'R'], ['i', 'I', '1', 'l', 'L', '|', '!'], ['c', 'C', '[', '{', '(', '<'], ['h', 'H', '#'], ['e', 'E', '3']]
	et le résultat du product() :
	['briche', 'brichE', 'brich3', 'bricHe', 'bricHE', 'bricH3', 'bric#e', 'bric#E', 'bric#3', 'briChe', 'briChE', 'briCh3', 'briCHe', 'briCHE', 'briCH3', 'briC#e', 'briC#E', 
	'briC#3', 'bri[he', 'bri[hE', 'bri[h3', 'bri[He', 'bri[HE', 'bri[H3', 'bri[#e', 'bri[#E', 'bri[#3', 'bri{he', 'bri{hE', 'bri{h3', 'bri{He', 'bri{HE', 'bri{H3', 'bri{#e',
	'bri{#E', 'bri{#3', 'bri(he', 'bri(hE', 'bri(h3', 'bri(He', 'bri(HE', 'bri(H3', 'bri(#e', 'bri(#E', 'bri(#3', 'bri<he', 'bri<hE', 'bri<h3', 'bri<He', 'bri<HE', 'bri<H3', 
	'bri<#e', 'bri<#E', 'bri<#3', 'brIche', 'brIchE', 'brIch3', 'brIcHe', 'brIcHE', 'brIcH3', 'brIc#e', 'brIc#E', 'brIc#3', 'brIChe', 'brIChE', 'brICh3', 'brICHe', 'brICHE', 
	'brICH3', 'brIC#e', 'brIC#E', 'brIC#3', 'brI[he', 'brI[hE', 'brI[h3', 'brI[He', 'brI[HE', 'brI[H3', 'brI[#e', 'brI[#E', 'brI[#3', 'brI{he', 'brI{hE', 'brI{h3', 'brI{He', 
	'brI{HE', 'brI{H3', 'brI{#e', 'brI{#E', 'brI{#3', 'brI(he', 'brI(hE', 'brI(h3', 'brI(He', 'brI(HE', 'brI(H3', 'brI(#e', 'brI(#E', 'brI(#3', 'brI<he', 'brI<hE', 'brI<h3',...]
	'''
	outListe=[]
	for line in fd:
		#print("la ligne vaut {}".format(line))
		dicto=[]
		# lecture lettre par lettre
		letters=[]
		for lettre in line.strip():
			# initialisation d'une liste pour la subs
			# print(lettre)
			if lettre in subDictLIGHT.keys():
				letters.append(subDictLIGHT[lettre])
			else:
				letters.append(lettre)
			#print("la liste vaut maintenant : ", letters)
		for item in product(*letters):
			outListe.append(''.join(item)) # equivaut a str.join('',item)
	return outListe # on retourne la liste de tous les pass genere

# ------------------------ #
def doAddMore(in_liste):
	outListe=[]
	listeMore=[''.join(p) for n in range(1,5) for p in product(numbersOnly, repeat=n)]

	for i in in_liste:
		for j in listeMore:
			outListe.append(i+j)
			outListe.append(i+j+"!")			
			for k in specChar:
				outListe.append(i+k+j)
				outListe.append(i+k+j+"!")
	return outListe

# ------------------------ #
def cmd_line(args):
	parser = argparse.ArgumentParser(description='Generate list of common syntax account name from list')
	parser.add_argument('-o','--outputfile',dest='outputfile',default='stdout', help="file generate with all account names, default stdout")
	requiredNamed = parser.add_argument_group('required named arguments')
	requiredNamed.add_argument('-i','--inputfile',dest='inputfile',default=False, required=True, help="file with each lines like : \"firstname name\"")
	return parser.parse_args()

# ------------------------ #
def writeOutputfile(inOutputfile,inList):
	try:
		with open(inOutputfile,'w') as outputFile:
			for x in inList:
				outputFile.write(x+"\n")
			for y in doAddMore(inList):
				outputFile.write(y+"\n")
		outputFile.close()
		return(0)
	except Exception as e:
		print("Error: An error accur while opening file: \"{}\" to write in".format(inArgs.inputfile))
		return(3)	

# ------------------------ #
# function to open file with input words
def openFile(inArgs):
	try:
		with open(inArgs.inputfile,'r') as inputFile:
			la_liste = doSubstitution(inputFile)

		if inArgs.outputfile == "stdout":
			for x in la_liste:
				print(x)
			for xx in doAddMore(la_liste):
				print(xx)
		else:
			writeOutputfile(inArgs.outputfile,la_liste)

		
	except FileNotFoundError as e:
		print('Error: file not found: {}'.format(inArgs.inputfile))
		exit(1)
	except PermissionError as e:
		print('Error: you don\'t have the right for this file')
		exit(2)
	except exception as e:
		print('Error: Critical Error with the file {}'.format(inArgs.inputfile))
		exit(3)
	
# ------------------------ #
# Start of the script
if __name__ == "__main__":
	args = cmd_line(sys.argv)
	exit(openFile(args))