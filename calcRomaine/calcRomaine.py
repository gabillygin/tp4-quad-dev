from calcRomaine.lettre_switcher import val_lettre
from numpy import zeros


def romain_to_decimal(chiffre_romain):
    total = 0
    nb_add = 0
    len_chiffre_romain = len(chiffre_romain)
    tab_decimal = zeros(len_chiffre_romain, int)

    for pos in range(len_chiffre_romain):
        tab_decimal[pos] = val_lettre(chiffre_romain[pos])
    print(chiffre_romain)
    if len_chiffre_romain > 1:
        while nb_add < len_chiffre_romain - 1:
            if tab_decimal[nb_add] < tab_decimal[nb_add + 1]:
                total -= tab_decimal[nb_add]
                nb_add += 1
                print("oui")
            total += tab_decimal[nb_add]
            nb_add += 1
        if nb_add != len_chiffre_romain:
            total += tab_decimal[nb_add]
            nb_add += 1
    else:
        total += tab_decimal[nb_add]

    return total


def add(num1, num2):
    return num1 + num2


def sous(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    if num2 != 0:
        return num1 / num2
    return -1

def caltos_romaine(nb_rom_1,nb_rom_2,signe):
    if signe == '+':
        return add(romain_to_decimal(nb_rom_1),romain_to_decimal(nb_rom_2))
    elif signe == '/':
        return div(romain_to_decimal(nb_rom_1),romain_to_decimal(nb_rom_2))
    elif signe == '*':
        return mul(romain_to_decimal(nb_rom_1),romain_to_decimal(nb_rom_2))
    elif signe == '-':
        return sous(romain_to_decimal(nb_rom_1),romain_to_decimal(nb_rom_2))
    else:
        print("Le signes n'est pas connu.")
        return -1
