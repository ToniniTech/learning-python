""" Sumar """
def sumar(num1, num2):
    suma = num1 + num2
    return suma

print(sumar(10,20))

""" Muestra la tabla de 7 del 1 al 10 """

def multiplicar7():
    for i in range(11):
        print(i*7)


print(multiplicar7())


""" Devuelve una lista sin elementos duplicados """

lst_sucia = [1,5,78,3,2,4,5,7,8,9,2,1,3,5,6,7,8,9,4,2,1,5,6,432,12,34,56,7,8,96,3]

def filtrar_lst(lst):
    new_lst = []
    for i in lst:
        if not i in new_lst:
            new_lst.append(i)
    return new_lst

print(filtrar_lst(lst_sucia))