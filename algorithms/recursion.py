# Practiquemos recursión.


# Factorial de un número

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# Suma de los dos primeros numeros naturales

def suma_n(n):
    if n == 0:
        return 0
    return n + suma_n(n-1)

print(suma_n(10))



