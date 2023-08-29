num1 = 42 # declaracion de variable; entero 
num2 = 2.3 # declaracion de variable ; flotante
boolean = True # declaracion de variable ; booleana
string = 'Hello World' # declaracion de variable ; cadena string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # declaracion de variable; lista  
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # declaracion de variable; diccionario
fruit = ('blueberry', 'strawberry', 'banana') # declaracion de variable; tupla
print(type(fruit)) # funcion print; funcion type de una lista
print(pizza_toppings[1])# funcion print del indice 1 de la lista pizza_toppings
pizza_toppings.append('Mushrooms') # error por no declarar la variable antes.
print(person['name']) # funcion print del contenido del indice name del diccionario person.
person['name'] = 'George' # asignacion de nombre al indice name del diccionario person
person['eye_color'] = 'blue' # asignacion de color al indice eye color del diccionario person
print(fruit[2]) # funcion print del indice 2 de la tupla fruit

if num1 > 45: # condicional if la variable numerica num1 es mayor a 45:
    print("It's greater") # imprime "It´s greater"
else: # condicional else si la condicion anterior no se cumple:
    print("It's lower") # imprime la cadena "It´s lower"

if len(string) < 5: # condicional if si el largo de la cadena es menor a 5:
    print("It's a short word!") # imprima la cadena contenida
elif len(string) > 15: # condicional  si la longitud de la cadena es mayor a 15:
    print("It's a long word!") # imprime la cadena contenida.
else: # condicional si ninguna de las condiciones anteriores se cumple:
    print("Just right!") # imprime la cadena de caracteres contenidas.

for x in range(5): # bucle for de un rango de 0 a 5 de 1 en 1
    print(x) # imprime x por cada iteracion (5)
for x in range(2,5): # bucle for de un rango de 2 a 5 de 1 en 1
    print(x) # imprime x por cada iteracion (5)
for x in range(2,10,3): # bucle for de un rango de 2 a 10 de 3 en 3.
    print(x) # imprime x por cada iteracion (2)
x = 0 # declaracion de variable numerica en 0; inicia el ciclo while en 0
while(x < 5):# mientras la variable numerica sea menor a 5:
    print(x) # imprime por x por cada iteracion...
    x += 1 # ... suma 1 a x 

pizza_toppings.pop() # error
pizza_toppings.pop(1)# quita el indice 1 de la lista pizza_toppings

print(person) # imprime el diccionario person completo
person.pop('eye_color') # error
print(person) # imprime el diccionario person completo

for topping in pizza_toppings: # recorre el diccionario pizza_toppings:
    if topping == 'Pepperoni': # topping es igual a "Pepperoni":
        continue # continua a la siguiente linea.
    print('After 1st if statement') # imprime la cadena de caracteres contenida en la funcion print
    if topping == 'Olives': # si la variable topping es igual a "Olives":
        break # Deten el ciclo for.

def print_hello_ten_times(): # declaracion de funcion print_hello_ten_times.
    for num in range(10): # inicia el ciclo for desde 0 a 10.
        print('Hello') # imprime "Hello" por cada iteracion (10)

print_hello_ten_times() # llamada a la funcion print_hello_ten_times.

def print_hello_x_times(x): # declaracion de la funcion print_hello_x_times, segun el parametro entregado x
    for num in range(x): # ciclo for del rango de 0 a x de 1 en 1.
        print('Hello') # en cada iteracion imprime "Hello"

print_hello_x_times(4) # llamada a la funcion print_hello_x_times con un paramtro de 4.

def print_hello_x_or_ten_times(x = 10): # declaracion de la funcion print_hello_x_or_ten_times con un parametro asignado de 10 veces
    for num in range(x): # ciclo for de rango de 0 a x de 1 en uno
        print('Hello') # imprime Hello por cada iteracion

print_hello_x_or_ten_times() # llamada a la funcion print_hello_x_or_ten_times
print_hello_x_or_ten_times(4) # llamada a la funcion print_hello_x_or_ten_times con el parametro 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)