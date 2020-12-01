def lettre_i():
    return 1


def lettre_v():
    return 5


def lettre_x():
    return 10


def lettre_l():
    return 50


def lettre_c():
    return 100


def lettre_d():
    return 500


def lettre_m():
    return 1000


def val_lettre(lettre):
    if lettre == 'I':
        return lettre_i()
    elif lettre == 'V':
        return lettre_v()
    elif lettre == 'X':
        return lettre_x()
    elif lettre == 'L':
        return lettre_l()
    elif lettre == 'C':
        return lettre_c()
    elif lettre == 'D':
        return lettre_d()
    elif lettre == 'M':
        return lettre_m()