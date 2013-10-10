import re
import datetime
liste_mois = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 
'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']
reponse = 0
while (type(reponse) != str):
   reponse = input('Quel est date de naissance ("xx/yy/zzzz") ?\n')

[jour, mois, annee] = map(lambda x:int(x), re.split('/', reponse))

print('Vous etes ne le %d %s %d' % (jour, liste_mois[mois-1],annee))

aujourdhui = datetime.date.today()
diff_ans = aujourdhui.year - annee
diff_jour = aujourdhui.day - jour
diff_mois = aujourdhui.month - mois 

if diff_ans < 0 :
   print("vous n'etes pas en cornet (haha), revenez bientot")
elif diff_ans <= 2:
    print("vous etes trop jeune pour taper au clavier")
else:
    if diff_mois >= 1:
        print ('vous avez %d ans ' % diff_ans)
    elif diff_mois == 0 and diff_jour >= 0:
        print ('vous avez %d ans' % diff_ans)
    elif diff_mois < 0:
        print ('vous avez %d ans' % diff_ans - 1)
