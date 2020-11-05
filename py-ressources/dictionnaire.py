#/usr/bin/python3
# -*- coding: utf-8 -*-

la_liste = ['thierry','audrey','sabrina','thierry','briche','robin','emie','briche','micchi']

# Le slicing : permet de trancher des parties de la liste [incide_depart::pas]
# la fonction zip() permet d'associer dans le retour plusieurs elements
# la fonction upper() permet de mettre en MAJUSCULE
# la fonction capitalize() permet de mettre seulement la premiere lettre en MAJ

dico = {name.upper() : firstname.capitalize() for name, firstname in zip(la_liste[::2], la_liste[1::2])}
print(dico)
