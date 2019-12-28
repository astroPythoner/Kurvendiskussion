from random import randint
from Funktion import Funktion, polynom_to_str

def fakultät(n):
    if n == 0:
        return 1
    erg = 1
    for x in range(1,n+1):
        erg *= x
    return erg

def alle_kombis_addieren(zahlen,länge_kombis):
    if länge_kombis == 1:
        erg = 0
        for i in range(len(zahlen) - länge_kombis + 1):
            erg += zahlen[i]
    else:
        erg = 0
        for i in range(len(zahlen)-länge_kombis+1):
            j = alle_kombis_addieren(zahlen[i+1:],länge_kombis-1)
            erg += zahlen[i]*j
    return erg

def get_random_polynomfunktion(höchster_exponent,min_nullstelle=-5,max_nullstelle=5):
    """gibt eine zufällige polynomfunktion mit höchster_exponent bei dem alle Nullstellen erratbar sind"""
    nullstellen = []
    for x in range(höchster_exponent):
        nullstellen.append(randint(min_nullstelle,max_nullstelle))
    return_funktion = "x'"+str(höchster_exponent)
    for expo in range(höchster_exponent):
        current_exponent = höchster_exponent-expo-1
        vor_faktor = alle_kombis_addieren(nullstellen,expo+1)
        return_funktion += polynom_to_str(vor_faktor,current_exponent)
    return Funktion(return_funktion)