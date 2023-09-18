#1. CUENTA REGRESIVA: crea una función que acepte un número como entrada. Devuelve una lista
# nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (cómo último elemento):
# Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]

def countdown(numero):
    lista = []
    i = numero
    while i > -1:
        lista.append(i)
        i -= 1
    return lista

print(countdown(10))

#2. IMPRIMIR Y DEVOLVER: crea una funcion que reciba una lista con dos numeros. Imprime el primer valor
# y devuelve el segundo.
# Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2.

def imprimir_y_devolver(lista):
    print(lista[0])
    return lista[1]

print(imprimir_y_devolver([2,4]))

#3. PRIMERO MAS LONGITUD: crea una funcion que acepte una lista y devuelva la suma del primer valor de
# la lista, mas la longitud de la lista.
# Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 + largo:5)

def primero_mas_longitud(lista):
    suma = lista[0] + len(lista)
    return suma

print(primero_mas_longitud([3,5,672,3]))

#4. VALORES MAYORES QUE EL SEGUNDO: escribe una funcion de que acepte una lista y cree una nueva
# que contenga solo los valores de la lista original que sean mayores que su segundo valor.
# imprime cuantos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos,
# has que la funcion devuelva False. 
# Ejemplo: valores_mayores_que_el segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
# Ejemplo: valores_mayores_que_el segundo([3]) debe devolver False.
def valores_mayores_que_el_segundo(lista):
    lista2 = []
    if len(lista) < 2:
        return False
    else:
        for i in lista:
            if i > lista[1]:
                lista2.append(i)
        return len(lista2), lista2

print(valores_mayores_que_el_segundo([5,2,3,2,1,4]))

#5. ESTA LONGITUD, ESE VALOR: escribe una funcion que acepte dos enteros como parametros: tamaño y valor.
# La funcion debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos
# el valor dado.
# Ejemplo: lenght_and_value(4,7) debe devolver [7,7,7,7]
# Ejemplo: lenght_and_value(6,2) debe devolver [2,2,2,2,2,2]


def lenght_and_value(largo,valor):
    lista = []

    for i in range(largo):
        lista.append(valor)
    
    return lista

print(lenght_and_value(4,7))
print(lenght_and_value(6,2))
