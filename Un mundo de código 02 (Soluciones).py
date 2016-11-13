"""
Ejercicio 01.10. Escribir dos funciones que permitan calcular:

La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
La cantidad de horas, minutos y segundos de un tiempo dado en segundos.

def HMSToSeg(h,m,s):
    return ((h*60)+m)*60+s
def SegToHMS(s):
    horas = s//3600
    s = s%3600
    minutos = s//60
    segundos = s%60
    return (horas,minutos,segundos)

Ejercicio 01.11. Usando las funciones del ejercicio anterior, escribir un programa que lea de teclado dos tiempos expresados en horas, minutos y segundos; las sume y muestre el resultado en horas, minutos y segundos por pantalla.

leyendo = True
while leyendo:
    try:
        h1 = int(input ("Introduce horas    1: "))
        m1 = int(input ("Introduce minutos  1: "))
        s1 = int(input ("Introduce segundos 1: "))
        h2 = int(input ("Introduce horas    2: "))
        m2 = int(input ("Introduce minutos  2: "))
        s2 = int(input ("Introduce segundos 2: "))
        leyendo = False
    except:
        print("Error en la introducción de datos\n")
(h, m, s) = SegToHMS(HMSToSeg(h1, m1, s1) + HMSToSeg(h2, m2, s2))
print ("La suma es:",h ,"horas" ,m ,"minutos y" ,s ,"segundos")


Ejercicio 01.12. Escribir una función que dados cuatro números, devuelva el mayor producto de dos de ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto más grande que se puede obtener entre ellos.

def mayor_producto(n1,n2,n3,n4):
    mayor = n1 * n2
    n1n3 = n1 * n3
    n1n4 = n1 * n4
    n2n3 = n2 * n3
    n2n4 = n2 * n4
    n3n4 = n3 * n4
    if n1n3 > mayor:
        mayor = n1n3
    elif n1n4 > mayor:
        mayor = n1n4
    if n2n3 > mayor:
        mayor = n2n3
    elif n2n4 > mayor:
        mayor = n2n4
    if n3n4 > mayor:
        mayor = n3n4
    return mayor

leyendo = True
while leyendo:
    try:
        num1 = int(input ("Introduce número 1 : "))
        num2 = int(input ("Introduce número 2 : "))
        num3 = int(input ("Introduce número 3 : "))
        num4 = int(input ("Introduce número 4 : "))
        leyendo = False
    except:
        print("Error en la introducción de datos\n")

print("El mayor producto entre ellos es: ", mayor_producto(num1,num2,num3,num4))


Ejercicio 01.13 Área de un triángulo en base a sus puntos:

1) Escribir una función que dado un vector al origen (definido por sus puntos x, y), devuelva la norma del vector, dada por (x^2 + y^2) ^ 1/2
http://www.ub.edu/glossarimateco/content/norma-de-un-vector
"""
def norma(x,y):
    return (x*x + y*y)**(1/2)

"""
2) Escribir una función que dados dos puntos en el plano (x1, y1 y x2, y2), devuelva la resta de ambos (debe devolver un par de valores).
"""
def resta(x1,y1,x2,y2):
    return (x1-x2, y1-y2)

"""
3) Utilizando las funciones anteriores, escribir una función que dados dos puntos en el plano (x1, y1 x2, y2), devuelva la distancia entre ambos.
"""
def distancia(x1,y1,x2,y2):
    (x,y)=resta(x1,y1,x2,y2)
    d=norma(x,y)
    if d < 0:
        d = -d
    return d
"""
4) Escribir una función que reciba un vector al origen (definido por sus puntos x, y) y devuelva un vector equivalente, normalizado (debe devolver un par de valores).
https://es.wikipedia.org/wiki/Vector_unitario
"""
def vector_unitario(x,y):
    n = norma(x,y)
    return (x/n, y/n)

"""
5) Utilizando las funciones anteriores ( 2) y 4) ), escribir una función que dados dos puntos en el plano (x1, y1 y x2, y2), devuelva el vector dirección unitario correspondiente a la recta que los une.
"""
def vector_unitario2(x1,y1,x2,y2):
    (x,y)=resta(x2,y2,x1,y1)
    return vector_unitario(x,y)

"""
6) Escribir una función que reciba un punto (x, y), una dirección unitaria de una recta (dx, dy) y un punto perteneciente a esa recta (cx, cy) y devuelva la proyección del punto sobre la recta.
(Notas.- Una recta puede estar definida por dos puntos o bien por un vector y un punto de la misma)

Diseño del algoritmo:

Al punto a proyectar (x, y) restarle el punto de la recta (cx, cy)
Obtener la matriz de proyección P, dada por: p11 = dx^2, p12 = p21 = dx * dy, p22 = dy^2.
Multiplicar la matriz P por el punto obtenido en el paso 1: rx = p11 * x + p12 * y, ry = p21 * x + p22 * y.
Al resultado obtenido sumar el punto restado en el paso 1, y devolverlo.

"""
def proyeccion(x,y,dx,dy,cx,cy):
    (t1,t2)=resta(x,y,cx,cy)
    p11 = dx*dx
    p12 = dx*dy
    p21 = p12
    p22 = dy*dy
    rx = p11 * t1 + p12 * t2
    ry = p21 * t1 + p22 * t2
    rx += cx
    ry += cy
    return (rx,ry)

"""


7) Escribir una función que calcule el área de un triángulo a partir de su base y su altura.
"""
def area_triangulo (b,h):
    return b*h/2
"""

8) Utilizando las funciones anteriores escribir una función que reciba tres puntos en el plano (x1, y1, x2, y2 y x3, y3) y devuelva el área del triángulo correspondiente.
"""
def area_vectorial (x1,y1,x2,y2,x3,y3):
    (dos_uno_x,dos_uno_y) = resta(x2,y2,x1,y1)
    (dos_tres_x,dos_tres_y) = resta(x3,y3,x1,y1)
    area = dos_uno_x * dos_tres_y - dos_uno_y * dos_tres_x
    if area < 0:
        area = -area
    return area/2

def area_proyeccion(x1,y1,x2,y2,x3,y3):
    base = distancia(x1,y1,x3,y3)
    (dx,dy) = vector_unitario2(x1,y1,x3,y3)
    (px,py) = proyeccion(x2,y2,dx,dy,x3,y3)
    altura =  distancia (x2,y2,px,py)
    return area_triangulo(base,altura)
