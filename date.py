import re
import datetime
aujourdhui = datetime.date.today()
liste_mois = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 
'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']
reponse = 0
while (type(reponse) != str):
   reponse = input('Quel est date de naissance ("xx/yy/zzzz") ?\n')

[jour, mois, annee] = map(lambda x:int(x), re.split('/', reponse))
print jour 
print mois
print annee
