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

# tuplas:
perro = ('Bruce', 'cocker spaniel', 19, False)
print(perro[0])
perro[1] = 'dachhund'

# listas
lista_vacia = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2])
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)
ninjas.pop()
print(ninjas)
ninjas.pop(1)
print(ninjas)

# diccionarios 
dic_vacio = {}
new_person = {'name': 'Jhon', 'edad': 38, 'peso': 160.2, 'usa_lentes': False}
print(dic_vacio)
print(new_person)
new_person['name'] = 'Jack'
print(new_person)
new_person['hobbies'] = ['escalada', 'programación']
print(new_person)
print(type(new_person['hobbies']))
w = new_person.pop('peso')
print(w)
print(new_person)

print(len(new_person))
print(new_person['name'],len(new_person['name']))

# cadenas
print('Esta es una cadena de ejemplo')

name = "Zen"
print("Mi nombre es", name)

name  = "Zen"
print("Mi nombre es " + name)

name = "Zen"
age = 20
print("Mi nombre es " + name + " y tengo " + str(age) + " años.")

# conversion
total = 35
user_val = "26"
#total  = total + user_val
total = total + int(user_val)
print(total)

# Cadenas "f" (interpolacion de cadenas literal)
first_name = "James"
last_name = "Bond"
age = 33
print(f"Mi nombre es {first_name} {last_name} y tengo {age} años de edad.")
print(f"Mi edad es {age} y me llamo {last_name}, {first_name} {last_name}.")
# string.format
print("Me llamo {}, {} {}.".format(last_name, first_name, last_name))
print("Mi perrito se llama {} y está super viejito. Tiene {} años de perro.".format(first_name, age))

hw = "Hola %s" % "mundo" 	# con valores literales
py = "Me encanta Python %d" % 3 
print(hw, py)
# salida: Hola mundo Me encanta Python 3
name = "Zen"
age = 27
print("Mi nombre es %s y tengo %d" % (name, age))		# o con variables
# salida: Mi nombre es Zen y tengo 27












































