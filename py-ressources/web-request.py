import requests
import re


# on initie une session de navigation
s = requests.session()

# on lance la requete et on recup le resultat
url = "http://challenge01.root-me.org/programmation/ch1/"
res = s.get(url)

# Voici un exemple de result :
'''
<html><body><link rel='stylesheet' property='stylesheet' id='s' type='text/css' href='/template/s.css' media='all' />
<iframe id='iframe' src='https://www.root-me.org/?page=externe_header'>
</iframe>U<sub>n+1</sub> = [ -8 + U<sub>n</sub> ] - [ n * 5 ]<br />
U<sub>0</sub> = 817
<br />You must find U<sub>703655</sub><br /><br />You have only 2 seconds to send the result with the HTTP GET method (at http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result=...)</body></html>
'''

print (res.text)

patternQuestion = r'You must find U\<sub\>(\d+)\<'
patternV1 = r'sub\> \= \[ (\-?\d+) \+'
patternV2 = r'n \* (\-?\d+) \]'
patternVU = r'\>0\<\/sub\> = (\-?\d+)'

question = re.findall( patternQuestion ,res.text)
theQuestion = int(question[0])
print("la question est {}".format(theQuestion))

var1 = re.findall( patternV1 ,res.text)
theVar1 = int(var1[0])
print("la var 1 est {}".format(theVar1))

var2 = re.findall( patternV2 ,res.text)
theVar2 = int(var2[0])
print("la var 2 est {}".format(theVar2))

varU = re.findall( patternVU ,res.text)
theVarU = int(varU[0])
print("U0 est {}".format(theVarU))
liste=[theVarU]

for i in range(0,theQuestion+1):
	liste.append((theVar1 + liste[i]) - (i * theVar2))

# print "Ui vaut {} et Ui+1 vaut {}".format(liste[i],liste[i+1])
	




laRep = str(liste[theQuestion])
print("la rep est {}".format(laRep))
# on pousse la rep et on affiche :
url2 = "http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result="+laRep
res2 = s.get(url2)
print (res2.text)


