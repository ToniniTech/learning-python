#Write a function that accepts two integers and returns the remainder of dividing the larger value by the smaller value.

#Division by zero should return an empty value.

def remainder(a,b):
    if min(a,b) == 0:
        return None
    elif a > b:
        return a%b
    else:
        b%a

print(remainder(17,5))

# You were camping with your friends far away from home, but when it's time to go back, you realize that 
# your fuel is running out and the nearest pump is 50 miles away! 
# You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

#Considering these factors, write a function that tells you if it is possible to get to the pump or not.

# Function should return true if it is possible and false if not.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

# Create a method that takes as input a name, city, and state to welcome a person. 
# Note that name will be an array consisting of one or more values that should be joined together with one space between each, 
# and the length of the name array in test cases will vary

def say_hello(name, city, state):
    return f"Hello, {' '.join(name)}! Welcome to {city}, {state}!"

print(say_hello(['Anthony', 'Viveros'], 'santiago', 'Metropolitana'))


