def dos(cad):
    """ DocStream
    """
    print(cad[:2])

def tres(cad):
    """ DocStream
    """
    print(cad[-3:])

def cada_dos(cad):
    """ DocStream
    """
    cadena = ""
    for i in range(0, len(cad), 2):
        cadena += cad[i]
    print(cadena)

def inversa(cad):
    """ DocStream
    """
    salida = ""
    for i in range(len(cad)-1, -1, -1):
        salida += cad[i]
    print(salida)

def reflejo(cad):
    """ DocStream
    """
    salida = cad
    for i in range(len(cad)-1, -1, -1):
        salida += cad[i]
    print(salida)



def separar(cad):
    """ DocStream
    """
    salida = ""
    for i in range(len(cad)-1):
        salida = salida + cad[i] + ","
    salida += cad[len(cad)-1]
    return salida

def separar2(cad, rmax):
    """ DocStream
    """
    if rmax == 0:
        return cad
    salida = ""
    rep = 0
    for i in range(len(cad)-1):
        salida = salida + cad[i] + ","
        rep += 1
        if rep == rmax:
            salida = salida + cad[i+1:-1]
            break
    salida += cad[len(cad)-1]
    return salida



def cambiar(cad, car):
    """DocString
    """
    salida = ""
    for i in cad:
        if i == " ":
            salida += car
        else:
            salida += i
    return salida

def cambiar2(cad, car, rmax):
    """DocString
    """
    if rmax == 0:
        return cad
    salida = ""
    rep = 0
    long = len(cad)
    for i in range(long):
        if cad[i] == " ":
            salida += car
            rep += 1
            if rep == rmax:
                salida += cad[i+1:]
                break
        else:
            salida += cad[i]
    return salida



def cambiar_x(cad):
    """DocString
    """
    salida = ""
    digitos = "0123456789"
    for i in cad:
        if i in digitos:
            salida += "X"
        else:
            salida += i
    return salida

def cambiar_x2(cad, rmax):
    """DocString
    """
    if rmax == 0:
        return cad
    salida = ""
    rep = 0
    digitos = "0123456789"
    lon = len(cad)
    for i in range(lon):
        if cad[i] in digitos:
            salida += "X"
            rep += 1
            if rep == rmax:
                salida += cad[i+1:]
                break
        else:
            salida += cad[i]
    return salida


def puntos(cad):
    """DocString
    """
    salida = ""
    long = len(cad)
    for i in range(0, long - (long % 3), 3):
        salida = salida + cad[i:i+3] + "."
    salida += cad[-(long % 3):]
    return salida

def puntos2(cad, rmax):
    """DocString
    """
    if rmax == 0:
        return cad
    rep = 0
    salida = ""
    long = len(cad)
    for i in range(0, long - (long % 3), 3):
        salida = salida + cad[i:i+3] + "."
        rep += 1
        if rep == rmax:
            salida = salida + cad[i+3:]
            return salida
    salida += cad[-(long % 3):]
    return salida



import locale

def puntua1(cad):
    """DocString
    """
    try:
        return '{0:,}'.format(int(cad)).replace(",", ".")
    except TypeError:
        return -1

def puntua2(cad):
    """DocString
    """
    locale.setlocale(locale.LC_ALL, '')
    try:
        return locale.format("%d", int(cad), grouping=True)
    except TypeError:
        return -1

def puntua3(cad):
    """DocString
    """
    locale.setlocale(locale.LC_ALL, '')
    try:
        return '{:n}'.format(int(cad))
    except TypeError:
        return -1

def puntua4(cad):
    """DocString
    """
    long = len(cad)
    primeros = long % 3
    if primeros > 0:
        salida = cad[0:primeros]+"."
    else:
        salida = ""
    for i in range(long//3):
        salida = salida + cad[primeros+i*3:primeros+i*3+3] + "."
    return salida[:-1]

def siglas1(cad):
    """ DocString """
    cad = " " + cad.strip()
    sig = ""
    while True:
        i = cad.find(" ")
        if i != -1:
            cad = cad[i+1:]
            if cad[0] == " ":
                continue
            else:
                sig = sig + cad[0]
        else:
            return sig

def siglas2(cad):
    """DocString"""
    cad = " " + cad.strip()
    sig = ""
    i = cad.find(" ")
    while i != -1:
        cad = cad[i+1:]
        if cad[0] != " ":
            sig = sig + cad[0]
        i = cad.find(" ")
    return sig

def mayus(cad):
    """DocString
    """
    cad = cad.strip()+ " "
    sig = ""
    i = cad.find(" ")
    while i != -1:
        if i != 0:
            sig = sig + cad[0:i].capitalize() + " "
        cad = cad[i+1:]
        i = cad.find(" ")
    return sig[:-1]

def aes(cad):
    """DocString"""
    cad = " " + cad.strip() + " "
    i = cad.find(" ")
    sig = ""
    while i != -1:
        cad = cad[1:]
        encontrado = cad.find(" ")
        if (cad[0] in "aA") and (encontrado != -1):
            sig = sig + cad[0:encontrado] + " "
        cad = cad[encontrado:]
        i = cad.find(" ")
    return sig[:-1]

def consonantes(cad):
    """DocString"""
    con = ""
    for i in cad:
        if not i in "aeiouAEIOU":
            con += i
    return con

def vocales(cad):
    """DocString"""
    con = ""
    for i in cad:
        if i in "aeiouAEIOU ":
            con += i
    return con

def revocaliza(cad):
    """DocString"""
    revoca = ""
    voc = "aeiouaAEIOUA"
    for car in cad:
        if car in "aeiouAEIOU":
            revoca += voc[voc.find(car)+1]
        else:
            revoca += car
    return revoca

def palindromo(cad):
    """DocString"""
    cad_limpia = ""
    for car in cad:
        if car != " ":
            cad_limpia += car
    tramo1 = len(cad_limpia)//2
    tramo2 = tramo1 - (len(cad_limpia)+1)%2
    return cad_limpia[:tramo1] == cad_limpia[:tramo2:-1]

def subcadena(cad, subcad):
    """DocString
    """
    return cad.find(subcad) != -1

def alfa(cad1, cad2):
    """DocString
    """
    if cad1 < cad2:
        return cad1
    else:
        return cad2

def bin_to_dec(num):
    """DocString
    """
    dec = 0
    for car in num:
        dec *= 2
        if car == "1":
            dec += 1
    return dec
