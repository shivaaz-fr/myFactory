#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""  commentaire 
		sur plusieurs  
		lignes """

try:
	with open('mon_fichier.txt','r') as fic:
		for line in fic:
			print(line, end='')
except FileNotFoundError as e:
	print('Le fichier {} n\'existe pas.'.format(e.filename))
	exit(1)
except PermissionError as e:
	print("Droit de lecture absent sur le fichier {}".format(e.filename))
	exit(2)
except exception as e:
	print("une erreure a empêché l'ouverture du fichier: {}".format(e.strerror))
	exit(3)
