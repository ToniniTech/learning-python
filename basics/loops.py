#-----------------------------------------------------------------------------------------------------#
# 1) Imprimir numeros pares del 0 al 20

'''for num in range(20):
    if num % 2 == 0:
        print(num + 2)
'''

#--------------------------------------------------------------------------------------------------------
# 2) Contador inverso con while
'''x = 10
while x > 0:
    x -= 1
    print(x)
print('Despegue!')
'''
#----------------------------------------------------------------------------------------------------------
# 3) Sumar los primero 100 numeros naturales (1-100)
'''suma = []
for i in range(101):
    print(i)
    suma.append(i)
print(sum(suma))
'''
#-----------------------------------------------------------------------------------------------------------
'''# 4) Pedir números al usuario hasta que ingrese cero 
num = ""
number_list = []
while num != 0:
    num = int(input('Enter a num: '))
    number_list.append(num)
print(number_list)
print('Cero ingresado')'''

#-----------------------------------------------------------------------------------------------------------------
#5) Tabla de multiplicar
'''
num = int(input('Ingresa un número del 1-10: '))

def tabla_de_multiplicar():
    for i in range(11):
        multiplication = num * i
        print(f'{num} * {i} = {multiplication}')

tabla_de_multiplicar()'''

#-----------------------------------------------------------------------------------------------------------------
#6) Adivina el numero
'''
import random

user_input = None
random_number = random.randint(1,10)

while random_number != user_input:

    try:
        user_input = int(input('Enter a number (1 - 10): '))

    except ValueError: 
        print('Enter a valid number!')

print('Guessed it!')
'''
# -------------------------------------------------------------------------------------------------------------
#7) Suma solo de numero positivos. Pide 5 numeros al usuarios 

'''numbers = []
for i in range(5):
    user_num = int(input('Enter a number: '))
    if user_num < 0:
        continue
    numbers.append(user_num)
    suma = sum(numbers)
print(suma)'''

# ----------------------------------------------------------------------------------------------------------------

#8) Menú de opciones

# Muestra un menú en bucle hasta que el usuario elija "Salir"
# Opciones como: 1) Saludar, 2) Sumar 2 números, 3) Salir

'''menu = ('Saludar', 'Sumar', 'Negociar', 'Salir')

print('Elige una de la siguientes opciones: ')
for indice, i in enumerate(menu, start=1):  
    print(indice,')',i)
user_input = input('Enter a choice: ')
if user_input == '1':
    print('Salundado')
elif user_input == '2':
    print('Sumando')
elif user_input == '3':
    print('Negociando')
elif user_input == '4':
    print('Exiting....')
else:
    print('Invalid option')
'''
# --------------------------------------------------------------------------------------------
#9) Determina si un numero es primo o no 

'''for i in range(100):
    if i % 2 == 0 or i % 3 == 0 or i == 1:
        print(i, 'NO es primo')
    else:
        print(i, 'Es primo')'''

#9.1) Nested loops 

'''for z in range(3):
    for x in range(3):
        for j in range(3):
            for i in range(1,10):
                print(i, end="")
            print()
        print()
    print()'''

#------------------------------------------------------------------------------------------------
#10) Bucles anidados

'''for x in range(3):
    for y in range(10):
        print(y, end=" ")
    print(x)'''
#----------------------------------------------------------------------------------------------------------

'''rows = int(input('Enter a number of rows: '))
columns = int(input('Enter a numbers of columns: '))
symbol = input('Enter the symbol to use: ')


for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()'''

#-------------------------------------------------------------------------------------------------------------
# 11) Patron de asteriscos. 
'''rows = int(input('Enter a number of rows: '))
columns = int(input('Enter a numbers of columns: '))
symbol = input('Enter the symbol to use: ')


for x in range(rows):
    for y in range(columns):
        y -= 1
        print(y)
    print()'''

#------------------------------------------------------------------------------------------------------
# 12) Piramide simple

'''altura = 5
for i in range(1, altura+1):
    print('*'* i)'''

# -----------------------------------------------------------------------------------------------------

#13)  Piramide alineada la derecha
'''altura = 5
for i in range(1, altura+1):
    espacios = altura - i 
    print("" * espacios + "*" i)'''

#14) Piramide centrada simetricamente

'''altura = 5
for i in range(1, altura + 1):
    espacios = altura - i 
    astericos = 2 * i - 1 
    print(" " * espacios + "*" * astericos)'''

#15) Realiza una piramide invertida centrada

'''altura = 5
for i in range(altura, 0, -1):
    espacios = altura - i
    asteriscos = 2 * i - 1   
    print(" " * espacios + asteriscos * "*")'''


## 16) Realiza una piramide simple alineada a la derecha

'''altura = 5
for i in range(1, altura+1):
    espacios = altura - i
    asteriscos = 2 * i -1
    print( espacios * "  "+"*" * asteriscos)'''

# 17) Realicemos una matriz de 5x5 cuadrada.
# Recuerda que las matrices solo se pueden sumar si tienen el mismo orden, sino, no se puede realizar la suma.

''''MatrizA = [[1,2,3,4,5],
          [5,4,3,2,1],
          [10,20,30,40,50],
          [5,10,15,20,25],
          [34,26,17,6,9]]

MatrizB = [[1,2,3,4,5],
           [45,67,2,34,56],
           [14,78,8,9,5],
           [10,20,30,40,50],
           [1,7,42,57,80]]
'''
'''
for matriza in MatrizA:
    print(matriza)
# Iteramos sobre cada elemento para guardarlo en una lista vacia
matrizSuma = []
print('\nMatriz A: ')
for matriz in MatrizA:
    print(matriz)



print('\nMatriz B: ')
for matriz in MatrizB:
    print(matriz)

print()

for i in range(5):
    fila_suma = []
    for j in range(5):
        suma = MatrizA[i][j] + MatrizB[i][j]
        fila_suma.append(suma)
    matrizSuma.append(fila_suma)


# Imprimir la matriz suma de forma ordenada
print('Matriz resultante: ')
for fila in matrizSuma:
    print(fila)'''

#---------------------------------------------------------------------------------------------------------------------

# 18) Realicemos una resta matrices de 4x4 cuadrada.
# Recuerda que las matrices solo se pueden restar si tienen el mismo orden, sino, no se puede realizar la suma.

# Lista vacia donde guardaremos la nueva matriz
'''restaMatriz = []

MatrizA = [[1,2,6,4,5],
          [5,4,3,2,1],
          [10,20,44,40,50],
          [5,10,134,20,45],
          [34,26,13,6,12]]

MatrizB = [[1,2,3,4,5],
           [15,67,2,34,26],
           [14,12,8,9,53],
           [10,20,30,40,50],
           [27,7,42,57,80]]

# Visualizamos las matrices A y B

print('\nMatriz A: ')
for matriz in MatrizA:
    print(matriz)

print('\nMatriz B: ')
for matriz in MatrizB:
    print(matriz)

# Realizamos un for loop para iterar sobre cada elemento de las matrices

for i in range(4):
    fila_resta = []
    for j in range(4):
       resta = MatrizA[i][j] - MatrizB[i][j]
       fila_resta.append(resta)
    restaMatriz.append(fila_resta)
    
# Visualizamos la nueva lista de la resta de la Matriz A y Matriz B

print('\nLa matriz resultante: ')
for fila in restaMatriz:
    print(fila)'''

#------------------------------------------------------------------------------------------------------

# 18) Realicemos una multiplicación de matrices de 3x3 cuadrada.

# listas
'''matrizMul = []

MatrizA = [[1,2,6],
          [5,4,3],
          [10,20,44]]
          

MatrizB = [[1,2,3],
           [15,67,2],
           [14,12,8]]

#Visualizamos Matriz A y Matriz B

print('\nMatriz A: ')
for matriz in MatrizA:
    print(matriz)

print('\nMatriz B: ')
for matriz in MatrizB:
    print(matriz)

# Realiza un for loop para iterar sobre cada elemento de la lista

for i in range(3): # fila
    fila = []
    for j in range(3):
        suma = 0
        for z in range(3):
            suma += (MatrizA[i][z] * MatrizB[z][j])
        fila.append(suma)
    matrizMul.append(fila)


# Visualización de la lista formada

print('La matriz formada de la multiplicación de A y B: ')
for fila in matrizMul:
    print(fila)
'''

