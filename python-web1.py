import requests
from requests.auth import HTTPBasicAuth

print("NATAS 0")

# Création des variables du script
user = "natas0"
password = "natas0"
url = "http://natas0.natas.labs.overthewire.org/"

# Envoi de la requête avec l'authentificaiton HTTPBasicAuth
res = requests.get(url, auth=HTTPBasicAuth(user, password))

# Affichage de la réponse
print(res.text)


