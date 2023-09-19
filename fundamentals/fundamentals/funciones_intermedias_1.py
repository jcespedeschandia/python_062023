#1. ACTUALIZAR VALORES EN DICCIONARIOS:
#1.1 Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora deberia ser [[5,2,3], [15,8,9]]
x = [[5,2,3], [10,8,9]]
x[1][0] = 15
print(x)
#1.2 Cambia el "apellido" del primer alumno de 'Jordan' a 'Bryant'.                   *****
estudiantes = [{'first_name': 'Michael','last_name': 'Jordan'}, {'first_name': 'Jhon', 'last_name': 'Rosales'}]
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes[0])

#1.3 En el directorio_deportes, cambia "Messi" por "Andres".
directorio_deportes = {'basketball': ['Kobe', 'Jordan', 'James', 'Curry'], 'futbol': ['Messi', 'Ronaldo','Rooney']}
directorio_deportes['futbol'][0] = 'Andres'
print(directorio_deportes)

#1.4 Cambia el valor 20 en z a 30
z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30
print(z)

#2. ITERAR A TRAVES DE UNA LISTA DE DICCIONARIOS: 
# Crea una funcion iterateDictionary(some_list) para que, dada una lista de diccionarios, la funcion recorra cada diccionario
# de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:

def iterateDictionary(some_list):
    for i in some_list:
        print(i)
    return 

estudiantes = [
            {'first_name': 'Michael', 'last_name': 'Jordan'}, 
            {'first_name': 'John', 'last_name': 'Rosales'},
            {'first_name': 'KB', 'last_name': 'Tonel'}]

iterateDictionary(estudiantes)

#3. OBTENER VALORES DE UNA LISTA DE DICCIONARIOS:
# Crea una funcion iterateDictionary2(key_name, some_list) que, dada una lista de diccionarios y un nombre de clave, la
# función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', name)
# deberia generar:
# Michael
# John
# Mark
# KB

# y iterarteDictionary2('last_name', estudiantes) deberia generar:
# Jordan
# Rosales
# Guillen 
# Tonel

def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])

estudiantes = [
            {'first_name': 'Michael', 'last_name': 'Jordan'}, 
            {'first_name': 'John', 'last_name': 'Rosales'},
            {'first_name': 'KB', 'last_name': 'Tonel'}]


iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)

#4. ITERAR A TRAVES DE UN DICCIONARIO CON VALORES DE LISTA
# Crea una funcion printInfo(some_dict) que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada
# clave junto con el tamaño de su lista, y luego imprima los valores asociados desntro de la lista de cada clave.


def printInfo(some_dict):
    for key in some_dict:
        print(f"{len(some_dict[key])}, {key.upper()}")
        for item in some_dict[key]:
            print(item)
        
dojo = {'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'], 
        'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
        }

printInfo(dojo)