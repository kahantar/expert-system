#!/usr/bin/python
# -*-coding: utf-8 -*
import sys
import fonction
import erreur
import re

class Parse:
    def __init__(self, fichier):
        self.fichier = fichier
        self.proposition = []
        self.valeurprop = {}
        self.regle = {}
        self.resultat = []

    def searchproposition(self):
        for x in self.fichier:
            if x.isalpha() == True and (x in self.proposition) == False:
                self.proposition.append(x)
        for i in self.proposition:
            self.valeurprop[i] = 0
        

    def searchfait(self):
        ligne = self.fichier.split('\n\n')
        try:
            fait = fonction.returnfait(ligne[1].split('\n')[0])
        except:
            print("Erreur Syntaxe")
            sys.exit()
        for x in fait:
            self.valeurprop[x] = 1
    
    def searchresult(self):
        ligne = self.fichier.split('\n\n')
        try:
            result = fonction.returnresult(ligne[1].split('\n'), 1)
        except:
            try:
                result = fonction.returnresult(ligne[2].split('\n'), 0)
            except:
                print("Erreur Syntaxe")
                sys.exit()
        for x in result:
            self.resultat.append(x)

    def verifregle(self):
        try:
            ligne = self.fichier.split('\n\n')[0].split('\n')
        except:
            print("Erreur Syntaxe")
            sys.exit()
        for x in ligne:
            erreur.regle(x)
    
    def searchregle(self):
        ligne = self.fichier.split('\n\n')[0].split('\n')
        for x in self.resultat:
            valeur = fonction.depart(ligne, x, self.valeurprop, [x])
            if valeur[x] == 1:
                print("{0} est Vrai".format(x))
            else:
                print("{0} est Faux".format(x))  
        