print(type(20))
print(type(2j))
print(type(3.5))

enterosAflotantes = float(20)
flotantesAenteros = int(20)
enterosAimaginarios = complex(20)
imaginariosAenteros = int(20j)
print(enterosAflotantes)
print(flotantesAenteros)
print(enterosAimaginarios)
print(imaginariosAenteros)

numero_imaginario = 3 + 2j
parte_real = int(numero_imaginario.real)

print(parte_real)

import random
x = 0
while x < 50:
    print(random.randint(1, 12))
    x += 1

x = 12345
print(len(str(x)))

name = 'Zen'
print("Mi nombre es ", name)
print("Hola " + str(30))

total = 35
user_val = "26"
total = total + int(user_val)
# print(total)
print(total)

agente = '007'
nombre = 'James'
apellido = 'Bond'
print("Mi nombre es {}, {} {}. Soy el agente {}, al servicio de la corona.".format(apellido, nombre, apellido,agente))
print(f"Mi nombre es {apellido}, {nombre} {apellido}. Soy el agente {agente}, al servicio de la corona.")


## Funciones

def add(a,b):
    x = a + b
    return x 

y = add(2,3)
print(y)

###

def add(a = 1, b = 2):
    x = a + b
    return x 

y = add()
print(y)

def di_hola(nombre):
    print("Hola " + nombre)

di_hola('Joaquin')

## 
def flexCount(lowNum, highNum, mult):
    
    multiplos = []
    for i in range(lowNum, highNum + 1, 1):
        if i % mult == 0:
            multiplos.append(i)
    
    sumaMultiplos = 0
    for i in multiplos:
        sumaMultiplos += i
        
    return f"Los multiplos de {mult}  en el rango de [{lowNum} y {highNum}] son {multiplos} y su suma total es {sumaMultiplos}."

print(flexCount(20,30,3))

























































