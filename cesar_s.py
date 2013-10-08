from string import ascii_lowercase 


def cesar(clef, mot):
   alpha =  list(ascii_lowercase)
   decale = alpha[clef:] + alpha[:clef]
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

#def cesar_map(clef, mot):
#  from operator import add as colle
#  alpha = list(ascii_lowercase)
#  decale = alpha[clef:] + alpha[:clef]
#  table = {c:v for (c,v) in zip(alpha,decale) }
#  return reduce(colle, map(lambda x:table[x], mot))


from numpy import loadtxt
dico = loadtxt('dictionnaire',dtype=str).tolist()

message_code = 'hi owasg acwbg zo dvmgweis eis zsg aohvg'
phrase = message_code.split()

for clef in range(26):
    vrai = vraisemblance(dico, phrase, clef) 
    if vrai > 0:
        s = ''
        for mot in phrase:
            s += cesar(-clef,mot)+ ' '
        print 'clef: %2d, vraissemblance %2d: %s' % (clef, vrai,s)    
