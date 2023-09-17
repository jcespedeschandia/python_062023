#1) Básico: imprime todos los números enteros del 0 al 150.
for i in range(151):
    print(i)

#2) Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1000.
for i in range(1005):
    if i % 5 == 0:
        print(i)
#3) contar, a la manera de dojo: imprime números enteros del 1 al 100.
# Si es divisible por 5, imprime "Coding" en su lugar. Si es divisible por 10, imprime "Coding Dojo"
for i in range(1,100):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)
#4) Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500.000 e imprime la suma final
x = 0
for i in range(500000):
    if i % 2 != 0:
        print("Numero impar ", str(i))
        x += i
print("Suma total ", str(x))

#5) Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
for i in range(2018, 0, -4):
    print(i)

#6) Contador flexible: establece tres variables de mult. Por ejemplo, si lowNum = 2, higNum = 9 y mult = 3. 
# El bucle debe imprimir 3,6,9 (en lineas sucesivas).

lowNum = 2
higNum = 10
mult = 2
for i in range(lowNum, higNum + 1,1):
    if i % mult == 0:
        print(i)


