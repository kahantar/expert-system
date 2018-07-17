#!/usr/bin/python
import sys
import parse

if len(sys.argv) != 2:
    print("Erreur Parametre")
    sys.exit()    
chemin = sys.argv[1]
try:
    f = open(chemin, 'r')
except:
    print("Erreur Fichier")
else:
    fichier = f.read()
    parse = parse.Parse(fichier)
    parse.searchproposition()
    parse.searchfait()
    parse.searchresult()
    parse.verifregle()
    parse.searchregle()
    