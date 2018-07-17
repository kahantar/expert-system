import sys
import re

def nbegal(str):
    i = 0
    i = str.count("=>")
    if i != 1:
        print("Erreur Syntaxe")
        sys.exit(0)

# def erreurproposition(regle, proposition):
#     for x in regle:
#         if x.isalpha():
#             if re.search(x, proposition) is not None:
#                 print("Erreur Syntaxe")
#                 sys.exit(0)
            
def regerreur(str):
    regle = str.split("=>")
    reg = r"^\(*(!?[A-Z]\)*[+|^]\(*)*!?[A-Z]\)*$"
    regtwo = r"\([A-Z]\)"
    regthree = r"^\(*(!?[A-Z]\)*[+]\(*)*!?[A-Z]\)*$"  
    try:           
        if (re.search(reg, regle[0]) is None) or (re.search(regtwo, regle[0]) is not None):
                print("Erreur Syntaxe")
                sys.exit(0)
        elif (re.search(regthree, regle[1]) is None) or (re.search(regtwo, regle[1]) is not None):
                print("Erreur Syntaxe")
                sys.exit(0)
    except:
        sys.exit(0)

def countparenthese(str):
    x = str.count('(')
    y = str.count(')')
    if x != y:
        print("Erreur Syntaxe")
        sys.exit(0)        
        
def regle(str):
    nbegal(str)
    str = str.replace(' ', '')
    regerreur(str)
    countparenthese(str)