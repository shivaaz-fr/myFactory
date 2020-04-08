# on veut lire les caractères 7 à 10 et 21 à 25 du fichier seek-file-text.txt
# dont le contenu est :
# Hello GLMF !
# Fichier texte

try:
	with open('seek-file-text.txt', 'r') as fic:
		fic.seek(6)
		print(fic.read(4))
		fic.seek(21)
		print(fic.read(5))
except FileNotFoundError as e:
	print("le fichier {} n'existe pas".format(e.filename))
	exit(1)

