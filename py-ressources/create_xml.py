#/usr/bin/python3
# -*- coding: utf-8 -*-

# pour utiliser le module lxml : pip3 install lxml
# lxml est plus rapide que le module natif de python

from lxml import etree

root = etree.Element('series')
serie = etree.SubElement(root,'nom')
serie.set('lang','fr')
serie.set('titre','Docteur_Who')

personnages = ['Doc who','Rose Tyler','Mickey Smith']

for perso in personnages:
	personnage = etree.SubElement(serie,'personnage')
	personnage.text = perso

try:
	with open("serie.xml","w") as fic:
		fic.write(etree.tostring(root, pretty_print=True).decode('utf-8'))
except IOError:
	print("pb lors de l'écriture du fichier")
	exit(1)
