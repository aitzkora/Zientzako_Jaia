from operator import add as colle
def cesar(clef, mot):
  alpha= list('abcdefghijklmnopqrstuvwxyz')
  decale = alpha[-clef:] + alpha[:-clef]
  table = {c:v for (c,v) in zip(alpha,decale) }
  return reduce(colle, map(lambda x:table[x], mot))

def vraisemblance(dico, phrase, clef):
    s = 0
    for mot in phrase:
        if cesar(clef,mot) in dico:
           s += 1
    return s 
from numpy import loadtxt
dico = loadtxt('dictionnaire',dtype=str).tolist()
phrase = ['ohv', 'pdwkv', 'f','hvw','elhq']

for clef in range(16):
    if vraisemblance(dico, phrase, clef) > 0:
        s = ''
        for mot in phrase:
            s += ' '+ cesar(clef,mot)
        print s    
            
