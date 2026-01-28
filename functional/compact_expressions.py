# 1) Numero par o impar sin if 

#  by using if 
def es_par(n):
    if n %2 == 0:
        return True
    else:
        return False

print(es_par(11))

# by not using if 

def es_par2(n):
    return int(n % 2 == 0)

print(es_par2(6))

# 2) Edad minima para votar 

def puede_votar(edad):
    if edad >= 18:
        return int(True)
    else:
        return int(False)

print(puede_votar(19))

def puede_votar2(edad):
    return True if edad >= 18 else False

print(puede_votar2(19))

def puede_votar3(edad):
    return int(edad >= 18)

print(puede_votar3(17))


#3) Devolver el mayor sin if 

# Crea una función mayor (a,b) que devuelva el número mayor entre "a" y "b" sin usar if, ni max(), ni ternarios. 

def mayor(a,b): 
    return (a + b + abs(a - b)) // 2

print(mayor(10,14))




