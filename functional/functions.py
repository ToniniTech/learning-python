# 1) 

def greet(name):
    return f'Hi {name}, how are you?'

print(greet('Anthony'))

# 2)

def add(a,b):
    return a + b

print(add(10,10))

# 3) 

def power(base, exponent):
    return base**exponent

print(power(10,2))

# 4) 

def student(name, age, grade):
    return f'{name} is {age}y/o. He is in {grade} grade'

print(student('Anthony', 20, '4th'))

# 5) 

def sum_all(*args):
    suma = 0
    for i in args:
        suma += i
    return suma

print(sum_all(10,30,20,50,10,30))

# 6) 

def exponent_all(*numbers):
    exponentes = []
    for number in numbers:
        exponentes.append(number**2)
    return exponentes
       

print(exponent_all(10,20,30,40,50))

#------------------------------------------------


