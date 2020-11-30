from calcRomaine.lettre_switcher import val_lettre
from numpy import zeros

def romain_to_decimal(chiffre_romain):
    total = 0
    len_chiffre_romain = len(chiffre_romain)
    tab_decimal = zeros(len_chiffre_romain,int)
    for pos in range(len_chiffre_romain):
        tab_decimal[pos] = val_lettre(chiffre_romain[pos])


    for pos in range(len_chiffre_romain-1):
        if tab_decimal[pos+1] > tab_decimal[pos]:
            total += (tab_decimal[pos+1]-tab_decimal[pos])
            pos += 1
        else:
            total += tab_decimal[pos]
        if(pos == len_chiffre_romain-2):
            total += tab_decimal[pos+1]
        print(pos, ' ', len_chiffre_romain, ' ', total)
    return total
