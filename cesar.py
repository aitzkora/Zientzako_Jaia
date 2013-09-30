from string import ascii_lowercase 


def cesar(clef, mot):
  """
  mot_code(clef, mot)
  encode (ou decode avec une clef negatif) un mot selon le code cesar en utilisant
  la clef

  """
  from operator import add as colle
  alpha = list(ascii_lowercase)
  decale = alpha[clef:] + alpha[:clef]
  table = {c:v for (c,v) in zip(alpha,decale) }
  return reduce(colle, map(lambda x:table[x], mot))

def cesar_bourrin(clef, mot):
   alpha =  list(ascii_lowercase)
   decale = list(alpha)
   for i in range(len(alpha)-clef):
        decale[i] = alpha[i + clef]
   for i in range(clef):
        decale[len(alpha) -clef + i] = alpha[i]
   table = {} 
   for i in range(len(alpha)):
         table.update({alpha[i]:decale[i]})
   code = ''
   for i in range(len(mot)):
          code += table[mot[i]]
   return code

def vraisemblance(dico, phrase, clef):
    s = 0
    for mot in phrase:
        if cesar(-clef,mot) in dico:
           s += 1
    return s 



from numpy import loadtxt
dico = loadtxt('dictionnaire',dtype=str).tolist()

message_code = 'ohv pdwkv f hvw elhq'
phrase = message_code.split()

for clef in range(26):
    if vraisemblance(dico, phrase, clef) > 0:
        s = ''
        for mot in phrase:
            s += cesar(-clef,mot)+ ' '
        print 'pour la clef %d , le message peut etre : %s' % (clef, s)    
