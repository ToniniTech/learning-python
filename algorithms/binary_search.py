# realiza el algoritmo binary search 

numeros_range = []
for i in range(0, 100+1, 3):
    numeros_range.append(i)

def binary_search(lst, num):
    low = 0 # inicio 
    high = len(lst)-1 # final
    while low <= high:
        mid = (low + high) // 2 # punto medio de la lista
        guess = lst[mid] # variable que accede a las posiciones
        if guess == num:
            return mid
        if guess > num:
            high = mid - 1
        else:
            low = mid + 1
    return None

print(binary_search(numeros_range, 75))
print(numeros_range[25])
