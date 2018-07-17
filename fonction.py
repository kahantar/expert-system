import re
import sys

def returnfait(str):
    reg = r"^=[A-Z]{0,}$"
    if re.search(reg, str) is None:
        sys.exit()
    fait = str[1:]
    return fait

def returnresult(str, i):
    if str[i] == "":
        return returnresult(str, i+1)
    reg = r"^\?[A-Z]{0,}$"
    if re.search(reg, str[i]) is None:
        sys.exit()              
    result = str[i][1:]
    return result

def searchfirst(regle):
    for r in regle:
        if r == '^' or r == '|':
            return False
        elif r == '+':
            return True
    return True

def calcul(total, operateur, new):
    if operateur == '+':
        return total * new
    elif operateur == '|':
        if new == True or total == True:
            return True
        else:
            return False
    elif operateur == '^':
        if (new == False and total == True) or (new == True and total == False):
            return True
        else:
            return False

def searchcalcul(regle, valeur, dif, resultat):
    if regle[0].isalpha() == True:
        ret = valeur[regle[0]]
    else:
        ret = not valeur[regle[1]]
    i = 2
    while i < len(regle):
        if (regle[i].isalpha() == True) and (regle[i-1] != '!'):
            ret = calcul(ret, regle[i-1], valeur[regle[i]])
        elif (regle[i].isalpha() == True) and (regle[i-1] == '!'):
            ret = calcul(ret, regle[i-2], not valeur[regle[i]])            
        i+=1
    if dif == 'ko' and ret == True:
        return False
    elif dif == 'ko'and ret == False:
        return valeur[resultat]
    return ret


def depart(ligne, resultat, valeur, loop):
    for x in ligne:
        [regle, proposition, dif] = returnregle(x, resultat)
        if regle != 0:
            reg = r"[+|^]"
            total = re.split(reg, regle)
            for t in total:
                if t not in loop:
                    loop.append(t)
                    depart(ligne, t, valeur, loop)
            if valeur[proposition] == 0 or (valeur[proposition] == 1 and dif == 'ko'):
                valeur[proposition] = searchcalcul(regle, valeur, dif, resultat)
    return (valeur)      

def returnregle(str, resultat):
    str = str.replace(' ', '')
    [regle, proposition] = str.split("=>")
    regle = regle.replace('(', '').replace(')', '')
    proposition = proposition.replace('(', '').replace(')', '')
    find = proposition.split('+')
    for x in find:
        if x == resultat:
            return regle, x, "ok"
        elif x == '!'+resultat:
            return regle, x[1], "ko" 
    return 0, 0, 0