#!/usr/bin/python3
# -*- coding: utf-8 -*-

from itertools import product
listAll=[]
list1=['A','B','C','D']
list2=['1','2']

listAll.append(list1)
listAll.append(list2)

for i in product(*listAll):
	print(''.join(i))
