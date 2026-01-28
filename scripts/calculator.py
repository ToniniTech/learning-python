# Haz una calculadora como la que tienes en un tu escritorio

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicación(x, y):
    return x * y

def división(x, y):
    return x / y


while True: 
    operation = input('Ingresa una operación (+, -, *, /) o "q" to quit: ')

    if operation == 'q':
        break

    x = float(input('Ingresa un numero: '))
    y = float(input('Ingresa un numero: '))  

    if operation == '+':
        print('Results: ', suma(x, y))
    elif operation == '-':
        print('Result: ', resta(x, y))
    elif operation == '*':
        print('Result: ', multiplicación(x, y))
    elif operation == '/':
        print('Result: ', división(x, y))
    else:
        print('Operación invalidad')
    

#





