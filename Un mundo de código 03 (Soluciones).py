"""
Un mundo de código 3
3.1. Escribir funciones que resuelvan los siguientes problemas:
Dado un número entero n, indicar si es o no par.

def par(n):
    return n % 2 == 0

Dado un número entero n, indicar si es o no primo.

def primo(n):
    from math import sqrt
    primo = True
    for i in (2,sqrt(n)+1):
        if n % i == 0:
            primo = False
            break
    return primo

3.2. Escribir una implementación propia de la función abs, que devuelva el valor absoluto de cualquier valor que reciba.

def abs(n):
    if n < 0:
        n = -n
    return n

3.3. Escribir un programa que reciba una a una las notas del usuario, preguntando a cada paso si desea ingresar más notas, e imprimiendo el promedio correspondiente.

print ("Introduzca sus notas")
print ("====================")
i = 0
total = 0
masNotas = True
while masNotas:
    leyendo = True
    while leyendo:
        try:
           n = float(input("Introduzca nota :"))
           leyendo = False
        except:
           print("Introduzca un valor numérico")
    total += n
    i += 1
    leyendo = True
    while leyendo:
        respuesta = input("¿Otra nota? (S/N)")
        if respuesta in "SNsn":
            leyendo = False
    if respuesta in "Nn":
        masNotas = False
print("Su promedio es de", total / i,"puntos")

3.4. Escribir una función que reciba un número entero k e imprima su descomposición en factores primos.

def factPrimos(n):
    i = 2
    print(1)
    while n >= i:
        if n % i == 0:
            print(i)
            n//=i
        else:
            i+=1
    
3.5. Manejo de contraseñas

Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.

contrasena = "contra"
while True:
    con = input("Contraseña : ")
    if con == contrasena:
        print ("Contraseña correcta")
        break
    else:
        print("Contraseña errónea")

Modificar el programa anterior para que solamente permita una cantidad fija de intentos.

contrasena = "contra"
intentos = 3
while intentos:
    con = input("Contraseña : ")
    if con == contrasena:
        print ("Contraseña correcta")
        break
    else:
        print("Contraseña errónea")
        intentos -=1

Modificar el programa anterior para que después de cada intento agregue una pausa cada vez mayor, utilizando la función sleep del módulo time.

from time import sleep
contrasena = "contra"
maxIntentos = 5
intentos = maxIntentos
while intentos != 0:
    con = input("Contraseña : ")
    if con == contrasena:
        print ("Contraseña correcta")
        break
    else:
        print("Contraseña errónea")
        intentos -=1
        if intentos > 0:
            sleep(10-int(10/maxIntentos*intentos))
        

Modificar el programa anterior para que sea una función que devuelva si el usuario ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).

def passwords():
    from time import sleep
    contrasena = "contra"
    maxIntentos = 5
    intentos = maxIntentos
    while intentos != 0:
        con = input("Contraseña : ")
        if con == contrasena:
            print ("Contraseña correcta")
            return True
        else:
            print("Contraseña errónea")
            intentos -=1
            if intentos > 0:
                sleep(10-int(10/maxIntentos*intentos))
    return False

3.6. Utilizando la función randrange del módulo random, escribir un programa que obtenga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique sin son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número correcto.

from random import randrange
n = randrange(10)
while True:
    leyendo = True
    while leyendo:
        try:
           adivina = int(input("Adivina el número: "))
           leyendo = False
        except:
           print("Introduzca un valor numérico")
    if adivina == n:
        print("¡¡ Ese es !!")
        break
    elif adivina < n:
        print("El número es más alto")
    else:
        print("El número es más bajo")

3.7. Algoritmo de Euclides

Implementar en python el algoritmo de Euclides para calcular el máximo común divisor de dos números n y m, dado por los siguientes pasos.

Teniendo n y m, se obtiene r, el resto de la división entera de m/n.
Si r es cero, n es el mcd de los valores iniciales.
Se reemplaza m ← n, n ← r, y se vuelve al primer paso.
Hacer un seguimiento del algoritmo implementado para los siguientes pares de números: (15,9);(9,15); (10,8); (12,6).

def euclides(m,n):
    if m < n:
        cambio = m
        m = n
        n = cambio
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    return n

print (euclides(15,9), euclides(9,15), euclides(10,8), euclides(12,6))

3.8. Potencias de dos.

Escribir una función es_potencia_de_dos que reciba como parámetro un número natural, y devuelva True si el número es una potencia de 2, y False en caso contrario.

def es_potencia_de_dos(n):
    while n != 1:
        if (n % 2) == 0:
            n = n / 2
        else:
            return False
    return True


def es_potencia_de_dos_2(n):
    from math import log2
    exp = log2(n)
    return (exp == int(exp))

print (es_potencia_de_dos(1), es_potencia_de_dos_2(1))
print (es_potencia_de_dos(2), es_potencia_de_dos_2(2))
print (es_potencia_de_dos(59), es_potencia_de_dos_2(59))
print (es_potencia_de_dos(256), es_potencia_de_dos_2(256))

Escribir una función que, dados dos números naturales pasados como parámetros, devuelva la suma de todas las potencias de 2 que hay en el rango formado por esos números (0 si no hay ninguna potencia de 2 entre los dos). Utilizar la función es_potencia_de_dos, descrita en el punto anterior.

def suma_potencias_de_2(a,b):
    suma = 0
    for n in range(a,b+1):
        if es_potencia_de_dos(n):
            suma += n
    return suma
print (suma_potencias_de_2(6,15))

3.9. Números perfectos y números amigos

Escribir una función que devuelva la suma de todos los divisores de un número n, sin incluirlo.

def suma_divisores (n):
    from math import sqrt
    suma = 1
    for i in range(2,n//2+1):
        if n % i == 0:
            suma+=i
    return suma

print (suma_divisores (6))


Usando la función anterior, escribir una función que imprima los primeros m números tales que la suma de sus divisores sea igual a sí mismo (es decir los primeros m números perfectos).

def perfecto(m):
    n = 1
    for i in range(m):
        while n != suma_divisores(n):
            n += 1
        print(n)
        n += 1
    
perfecto(6)


Usando la primera función, escribir una función que imprima las primeras m parejas de números(a,b), tales que la suma de los divisores de a es igual a b y la suma de los divisores de b es igual a a(es decir las primeras m parejas de números amigos).

def perfectos(m):
    a = 0
    for i in range(m):        
        while True:
            a+=1
            b = suma_divisores(a)
            if suma_divisores(b)==a and a!=b and a < b :
                print(a,b)
                break
            
perfectos(10)

Proponer optimizaciones a las funciones anteriores para disminuir el tiempo de ejecución.

3.10. Escribir un programa que le pida al usuario que ingrese una sucesión de números naturales (primero uno, luego otro, y así hasta que el usuario ingrese -1 como condición de salida). Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total de los valores y el promedio.


3.11. Escribir una función que reciba dos números como parámetros, y devuelva cuántos múltiplos del primero hay, que sean menores que el segundo.

Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
Implementarla utilizando un ciclo while, que multiplique el primer número hasta que sea mayor que el segundo.
Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operaciones?

3.12. Escribir una función que reciba un número natural e imprima todos los números primos que hay hasta ese número.

3.13. Escribir una función que reciba un dígito y un número natural, y decida numéricamente si el dígito se encuentra en la notación decimal del segundo.

3.14. Escribir una función que dada la cantidad de ejercicios de un examen, y el porcentaje necesario de ejercicios bien resueltos necesario para aprobar dicho examen, revise un grupo de examenes. Para ello, en cada paso debe preguntar la cantidad de ejercicios resueltos por el alumno, indicando con un valor centinela que no hay más examenes a revisar. Debe mostrar por pantalla el porcentaje correspondiente a la cantidad de ejercicios resueltos respecto a la cantidad de ejercicios del examen y una leyenda que indique si aprobó o no.

3.15. Escribir una función que reciba por parámetro una dimensión n, e imprima la matriz identidad correspondiente a esa dimensión.

def matrizIdentidad(m):
    for i in range(m):
        linea = ""
        for j in range(m):
            if i!=j:
                linea += "0 "
            else:
                linea += "1 "
        print(linea)

matrizIdentidad (10)

3.16. Escribir funciones que permitan encontrar:

El máximo o mínimo de un polinomio de segundo grado (dados los coeficientes a, b y c), indicando si es un máximo o un mínimo.
Las raíces (reales o complejas) de un polinomio de segundo grado. Nota: validar que las operaciones puedan efectuarse antes de realizarlas (no dividir por cero, ni calcular la raiz de un número negativo).
La intersección de dos rectas (dadas las pendientes y ordenada al origen de cada recta). Nota: validar que no sean dos rectas con la misma pendiente, antes de efectuar la operación.
3.17. Escribir funciones que resuelvan los siguientes problemas:

Dado un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
Dado un mes, devolver la cantidad de dias correspondientes.
Dada una fecha (dia, mes, año), indicar si es válida o no.
Dada una fecha, indicar los dias que faltan hasta fin de mes.
Dada una fecha, indicar los dias que faltan hasta fin de año.
Dada una fecha, indicar la cantidad de dias transcurridos en ese año hasta esa fecha.
Dadas dos fechas (dia1, mes1, año1, dia2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y dias.
Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible.

3.18. Suponiendo que el primer dia del año fue lunes, escribir una función que reciba un número con el dia del año (de 1 a 366) y devuelva el dia de la semana que le toca. Por ejemplo: si recibe3 debe devolver miércoles, si recibe 9 debe devolver martes’.

3.19. Escribir un programa que reciba como entrada un año escrito en números arábigos y muestre por pantalla el mismo año escrito en números romanos.

3.20. Programa de astrologia: el usuario debe ingresar el dia y mes de su cumpleaños y el programa le debe decir a que signo corresponde. Nota:

Aries: 21 de marzo al 20 de abril.
Tauro: 21 de abril al 20 de mayo.
Geminis: 21 de mayo al 21 de junio.
Cancer: 22 de junio al 23 de julio.
Leo: 24 de julio al 23 de agosto.
Virgo: 24 de agosto al 23 de septiembre.
Libra: 24 de septiembre al 22 de octubre.
Escorpio: 23 de octubre al 22 de noviembre.
Sagitario: 23 de noviembre al 21 de diciembre.
Capricornio: 22 de diciembre al 20 de enero.
Acuario: 21 de enero al 19 de febrero.
Piscis: 20 de febrero al 20 de marzo.



Bórrame Esto es lo que he añadido. 
"""