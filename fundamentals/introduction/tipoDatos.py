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
print(string.upper(f"Mi nombre es {apellido}, {nombre} {apellido}. Soy el agente {agente}, al servicio de la corona."))















































