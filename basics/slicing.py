# 1) Accede al tercer elemento de una lista

'''lista = [10, 20, 30, 40, 50]

print(f'The value of the 3rd element: {lista[2]}')
'''
# 2) Access the last element using negative indexing

'''print(f'Last element: {lista[-1]}')'''

# 3) Get the first fours characters of a string

'''String1 = 'Arroz'

print(String1[0:4])'''

# 4) 🧩 Slice a list from the second to the fourth element

'''print(String1[2:4])
'''
# 5) Reverse a string using slicing 

'''print(String1[::-1].lower())
'''

# 6) ➖ Get all elements except the last one

'''print(String1[0:-1])
'''
# 7)  Access the main diagonal of a matrix

'''MatrixB = [[12, 35, 21],
           [12, 15, 34],
           [12, 54, 67]]
'''
'''
for i in range(len(MatrixB)):
    print(MatrixB[i][-i-1])'''

#8) Extract the last three elements of a list
'''
string2 = 'Arrocito'

print(string2[5:8])'''

#9) 🧭 Use slicing with step to get elements in even positions
numbers = []
for i in range(21):
    numbers.append(i)
'''
even_positions = numbers[::2]
print(even_positions)
'''
#10) 🎯 Replace the third element of a list with another value

'''print(numbers)'''

numbers[2] = 1000
print(numbers) 