#/usr/bin/python3
# -*-coding: utf-8 -*-

# lecture du liste et affiche de chaque element 

la_liste = ['thierry','audrey','sabrina','thierry','briche','robin','emie','briche','micchi']

for num,name in enumerate(la_liste):
	print(num, name)

# la fonction enumerate() renvoi a chaque iteration un tuple compose de la position
# et l'element lui meme

print('---------')

# on pourrait également utiliser la fonction index() :
for name in la_liste:
	print(la_liste.index(name), name)

print('---------')

# suppression des doublons set(), et on trie sorted()
# rem: set() transforme la liste en ensemble qui ne peut pas contenir de doublon
#      il est donc necessaire de retransformer le retour de set() en list()
for name in sorted(list(set(la_liste))):
	print(name)

print('---------')



