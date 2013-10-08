import string

def cesar(clef, mot):

    return mot

def vraisemblance(dico, phrase, clef):
    s = 0
    for mot in phrase:
        if cesar(-clef,mot) in dico:
           s += 1
    return s 

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
