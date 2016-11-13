
#pylint: disable = i0011, c0103

#%%
"""
Ejercicio 1
===========
Escribir un programa que lea las palabras de un fichero words.txt
(http://www.pythonlearn.com/code3/words.txt) y las almacene como claves en un
diccionario. No importan los valores.
Posteriormente leer palabras desde teclado y utilizar el operador in como una
forma rápida de comprobar si las palabras están dentro del diccionario o no.
"""

try:
    fhandle = open("words.txt")
except IOError:
    print("El fichero no existe")
    exit()
text = fhandle.read()
word_list = text.split()
dictionary = dict()
for word in word_list:
    dictionary[word] = dictionary.get(word, 0) + 1

while True:
    word = input("Introduzca una palabra (* para fin): ")
    if word == "*":
        fhandle.close()
        break
    if word in dictionary:
        print("La palabra %s SÍ está en el texto")
    else:
        print("La palabra %s NO está en el texto")

#%%
"""
Ejercicio 2
===========
Escribe un programa que contabilice cada mensaje de correo electrónico
por el día de la semana en que se envió. El proceso buscará líneas que
comiencen con "From " mirarán la tercera palabra de la línea y resgistrará
la cuenta para cada día de la semana. Al final del programa visualizar
el contenido los totales de cada día.

Línea de ejemplo:
    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Ejemplo de ejecución:

Introduzca el nombre del fichero: mbox-short.txt
Lunes     : 299
Martes    : 372
Miércoles : 292
Jueves    : 392
Viernes   : 315
Sábado    :  61
Domingo   :  66
"""

try:
    fhandle = open(input("Introduzca el nombre del fichero: "))
except IOError:
    print("El fichero no existe")
    sys.exit()                      #pylint: disable = i0011, e0602
days_of_the_week = dict()
for line in fhandle:
    if line.startswith("From "):
        day = line.split()[2]
        days_of_the_week[day] = days_of_the_week.get(day, 0) + 1
day_es = ["Lunes    ", "Martes   ", "Miércoles", "Jueves   "
          , "Viernes  ", "Sábado   ", "Domingo  "]
day_en = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for day in range(7):
    print("%s : %3d" % (day_es[day], days_of_the_week[day_en[day]]))

#%%
"""
Ejercicio 3
===========
Escribir un programa que lea un log de correo construya un histograma usando
un diccionario para contar cuántos mensajes se recibieron de cada dirección
de correo electrónico y visualice los resultados.

Introduzca el nombre del fichero: mbox-short.txt

gopal.ramasammycook@gmail.com : 1
louis@media.berkeley.edu : 3
cwen@iupui.edu : 5
antranig@caret.cam.ac.uk : 1
rjlowe@iupui.edu: 2
gsilver@umich.edu: 3
david.horwitz@uct.ac.za: 4
wagnermr@iupui.edu: 1
zqian@umich.edu: 4
stephen.marquard@uct.ac.za: 2
ray@media.berkeley.edu: 1
"""

#%%
"""
Ejercicio 4
===========
Añadir código al programa anterior para averiguar quién tiene más mensajes en
el fichero.
Después de leer todos los datos y esté creado el diccionario buscar a través
del diccionario usando un bucle máximo (ver la sección [maximumloop]) para
encontrar quién tiene más mensajes y mostrar en pantalla cuántos mensajes
tenía esa persona.

Introduzca el nombre del fichero: mbox-short.txt
cwen@iupui.edu 5

Introduzca el nombre del fichero: mbox.txt
zqian@umich.edu 195
"""

#%%
"""
Ejercicio 5
===========
En esta ocasión hay que registrar el nombre de dominio (en lugar de la
direción) desde dónde los mensajes se enviaron en lugar de de quién vino el
mensaje.

This program records the domain name (instead of the address) where the
message was sent from instead of who the mail came from (i.e. the whole
email address).
 At the end of the program print out the contents of your dictionary.

Introduzca el nombre del fichero: mbox-short.txt
media.berkeley.edu: 4
uct.ac.za: 6
umich.edu: 7
gmail.com: 1
caret.cam.ac.uk: 1 iupui.edu: 8}
"""
