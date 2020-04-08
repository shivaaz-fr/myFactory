error = True

while error:
	try:
		entier = int(input("donne un nombre entier : "))
		error = False
	except:
		print("ceci n'est pas un entier....")

print("bien recu l'entier qui est {}".format(entier))	

laPhrase = input("donne une phrase ou un mot: ")
print ("la phrase est : {}".format(laPhrase))

error = True
while error:
	try:
		reels = list(map(float, input('donne des reels séparés par de virgule : ').split(',')))
		error = False
	except:
		print("Cela ne correspond pas à la demande...")

print("voici la liste de réel :{}".format(reels))

