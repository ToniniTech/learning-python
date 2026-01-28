import math 
# 1. 🔄 Swap two variables without using a third one

a = 5
b = 10

a, b = 10, 5

print(a)
print(b)

# 2. 🔢 Extract index and value using enumerate()

fruits = ['apple', 'banana', 'cherry']
# Print: Index: 0, Value: apple (and so on for all elements)

for index, value in enumerate(fruits):
    print(f'Index: {index+1}, Value: {value}')

#3. 🧱 Flatten a 2D list using a nested list comprehension

matrix = [[1, 2], [3, 4], [5, 6]]

flatten_list = [element for i in matrix for element in i]

print(flatten_list)

#4.💡 Create a list of squares for even numbers from 0 to 10 using list comprehension

numbers = [1,2,3,4,5,6,7,8,9,10]

square_evens = [square**2 for square in numbers if square % 2 == 0 ]

print(square_evens)

square_root = [math.sqrt(square) for square in numbers if square % 2 == 0]

print(square_root)

square_all_numbers = [math.sqrt(square) for square in numbers if square]

print(square_all_numbers)

# 🔍 Filter and return only odd numbers
numbers2 = []

for i in range(1,31):
    numbers2.append(i)    

odd_numbers = [odd for odd in numbers if odd %2 != 0]
print(odd_numbers)

odd_numbers2 = [odd for odd in numbers2 if odd %2 != 0]
print(odd_numbers2)

# 3. 🧮 Add 5 to every number in the list

numbers_plus = [suma*5  for suma in numbers]
print(numbers_plus)

# 4. 🔢 Convert a list of strings to their lengths

strings = ['Arrocito', 'Arepita', 'Manzana', 'Calavera', 'Mamawebo', 'Pequeñeces', 'Whatever']


strings_len = [len(string) for string in strings]

print(strings_len)

#5  Return words that start with a vowel
vowels = ['a','e','i','o','u']

words_vowel = [word for word in strings if word[0].lower() in vowels]

print(words_vowel)

#6 🎯 Filter numbers divisible by 3 and multiply them by 2


numbers6 =  [1, 3, 5, 6, 9, 10, 12]

divisible_by_3 = [number*2 for number in numbers6 if number % 3 == 0]

print(divisible_by_3)

# 7 . 🧩 Flatten a 2D list into a 1D list

given = [[1, 2], [3, 4], [5, 6]]

list = [element for row in given for element in row]
print(list)

# 8 🧵 Extract the first letter of each word

result = [string[0] for string in strings]
print(result)

# 9  Convert strings to uppercase only if they are longer than 3 characters

uppercase = [string.upper() for string in strings if len(string) > 7]
print(uppercase)

