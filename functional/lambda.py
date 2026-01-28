# Crea una lambda que sume dos números

suma = lambda num1, num2: num1 + num2

print(suma(10,20))

# Crea una lambda que calcule el cuadrado de un número

cuadrado = lambda x: x**2
print(cuadrado(10))

# Crea una lambda que reciba una palabra y devuelva su última letra

ultima = lambda x: x[-1]
print(ultima('python'))

# ⚙️ Nivel 2: Con funciones integradas (map, filter, reduce, sorted)

numeros = [1, 2, 3, 4, 5]
# Usa lambda y map para duplicar cada número

resultado = map(lambda x: x*2, numeros)
print(list(resultado))

# Filtrar pares con filter()

numeros = [1, 2, 3, 4, 5, 6] # filtrar solo numero pares
resultado = list(filter(lambda x: x % 2 == 0, numeros))

