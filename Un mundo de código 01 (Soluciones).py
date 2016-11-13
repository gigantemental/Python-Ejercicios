Ejercicio 01.02. Escribir un programa que le pregunte al usuario una cantidad de euros, una tasa de interés y un número de años y muestre como resultado el monto final a obtener. La fórmula a utilizar es:
Cn = C * (1 + x/100) ^ n
Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular.


def Cn (c,x,n):
    return c * (1 + x / 100) ** n

leyendo = True
while leyendo:
    try:
        c = float(input ("Introduce el capital: "))
        n = float(input ("Introduce los años  : "))
        x = float(input ("Introduce el interés: "))
        leyendo = False
    except:
        print("Error en la introducción de datos\n")
   
print("Total a pagar: ", Cn(c,x,n), "euros")


Ejercicio 01.03. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es: F = 9/5 * C + 32.


def fahrenheitToCelsius(c):
    return 9/5 * c + 32

leyendo = True
while leyendo:
    try:
        c = float(input("Introduzca temperatura en grados Celsius: "))
        leyendo = False
    except:
        print("Introduzca un valor numérico\n")

print ("La temperatura equivalente en grados Fahrenheit es :", fahrenheitToCelsius(c))


Ejercicio 01.04. Utilice el programa anterior para generar una tabla de conversión de temperaturas, desde 0º F hasta 120º F, de 10 en 10.


def fahrenheitToCelsius(c):
    return 9/5 * c + 32

print ("Grados Fahrenheit     Grados Celsius")
print ("=================     ==============")
for i in range(0,121,10):
    print ("      ",i,"               ",fahrenheitToCelsius(i))


Ejercicio 01.05. Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.


leyendo = True
while leyendo:
    try:
        inicial = int(input("Introduzca valor inicial: "))
        final   = int(input("Introduzca valor final: "))
        leyendo = False
    except:
        print("Introduzca solo valores numéricos enteros\n")
if inicial % 2 == 1:
    inicial+=1
for i in range(inicial,final+1,2):
    print(i)


Ejercicio 01.06. Escribir un programa que reciba un número n por parámetro e imprima los primeros números triangulares, junto con su índice.
Los números triangulares se obtienen mediante la suma de los números naturales desde 1 hasta n. Es decir, si se piden los primeros 5 números triangulares, el programa debe imprimir:
1 - 1
2 - 3
3 - 6
4 - 10
5 - 15
Nota: hacerlo usando y sin usar la ecuación n * (n + 1) / 2. ¿Cuál realiza más operaciones? (Respuesta: triangularIterativo con diferencia)


def triangularIterativo(n):
    triangular = 0
    for i in range(1,n+1):
        triangular +=i
    return triangular

def triangularCalculado(n):
    return int(n * (n+1)/2)

leyendo = True
while leyendo:
    try:
        n = int(input("Introduzca número de triangulares a calcular: "))
        leyendo = False
    except:
        print("Introduzca solo valores numéricos enteros\n")

for i in range(1,n+1):
    print (i,"  -  ",triangularIterativo(i))

print()

for i in range(1,n+1):
    print (i,"  -  ",triangularCalculado(i))


Ejercicio 01.07. Escribir un programa que tome una cantidad m de valores ingresados por el usuario, a cada uno le calcule el factorial e imprima el resultado junto con el número de orden correspondiente.


leyendo = True
while leyendo:
    try:
        m = int(input("Introduzca número factoriales a calcular: "))
        leyendo = False
    except:
        print("Introduzca solo valores numéricos enteros\n")

for i in range(1,m+1):
    leyendo = True
    while leyendo:
        try:
            n = int(input("Introduzca un número para calcular su factorial: "))
            leyendo = False
        except:
            print("Introduzca solo valores numéricos enteros\n")
    factorial = 1
    for j in range(2,n+1):
        factorial *= j
    print(i,n,factorial)


Ejercicio 01.08. Escribir un programa que imprima por pantalla todas las fichas de dominó, una por línea y sin repetir.


for i in range (7):
    for j in range (i,7):
        print(i,j)


Ejercicio 01.09. Modificar el programa anterior para que pueda generar fichas de un juego que puede tener números de 0 a n.


leyendo = True
while leyendo:
    try:
        n = int(input("Introduzca número máximo del dominó: "))
        leyendo = False
    except:
        print("Introduzca solo valores numéricos enteros\n")
for i in range (n+1):
    for j in range (i,n+1):
        print(i,j)

