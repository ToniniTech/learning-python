# realiza el algoritmo bubble sort

numeros = [3,5,78,1,23,567,532,12,34,566] # lista desordenada
def bubble_sort(lst):
    for i in range(len(lst)): # ciclo externo 
        for j in range(len(lst)-1-i):  # ciclo interno
            if lst[j] > lst[j+1]: 
                lst[j], lst[j+1] = lst[j+1], lst[j] # Se intercambias las posiciones Si se cumple la condición
    return lst

print(bubble_sort(numeros))