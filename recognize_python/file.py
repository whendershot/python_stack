num1 = 42 #variable declaration, numeric
num2 = 2.3 #variable declaration, numeric
boolean = True #variable declaration, boolean
string = 'Hello World' #variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, list initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, tuple initialize
print(type(fruit)) #function call, argument, tuple access value, log statement
print(pizza_toppings[1]) #function call, argument, list access value, log statement
pizza_toppings.append('Mushrooms') #function call, argument, list add value
print(person['name']) #function call, argument, dictionary access value, log statement
person['name'] = 'George' #dictionary change value
person['eye_color'] = 'blue' #dictionary add value
print(fruit[2]) #function call, argument, tuple access value, log statement

if num1 > 45: #conditional if
    print("It's greater") #function call, argument, log statement
else: #conditional else
    print("It's lower") #function call, argument, log statement

if len(string) < 5: #conditional if, function call, argument, length check
    print("It's a short word!") #function call, argument, log statement
elif len(string) > 15: #conditional else if, function call, argument, length check
    print("It's a long word!") #function call, argument, log statement
else: #conditional else
    print("Just right!") #function call, argument, log statement

for x in range(5): #for loop, function call, argument, variable declaration
    print(x) #function call, argument, log statement
for x in range(2,5): #for lopp, function call, argument, variable declaration
    print(x) #function call, argument, log statement
for x in range(2,10,3): #for loop, function call, argument, variable declaration
    print(x) #function call, argument, log statement
x = 0 #variable declaration, numeric
while(x < 5): #while loop, variable declaration
    print(x) #function call, argument, log statement
    x += 1 #increment value

pizza_toppings.pop() #function call, list delete value
pizza_toppings.pop(1) #function call, list delete value

print(person) #function call, argument, log statement
person.pop('eye_color') #function call, argument, dictionary delete value, access value
print(person) #function call, argument, log statement

for topping in pizza_toppings: #for loop, variable declaration, list access value
    if topping == 'Pepperoni': #type check
        continue #continue
    print('After 1st if statement') #function call, argument, log statement
    if topping == 'Olives': #type check
        break #break

def print_hello_ten_times(): #function declaration
    for num in range(10): #for loop, variable declaration, funciton call, argument
        print('Hello') #function call, argument, log statement

print_hello_ten_times() #function call

def print_hello_x_times(x): #function declaration, parameter
    for num in range(x): #for loop, variable declaration, function call, argument
        print('Hello') #function call, argument, log statement

print_hello_x_times(4) #function call, argument

def print_hello_x_or_ten_times(x = 10): #function declaration, parameter
    for num in range(x): #for loop, variable declaration, function call, argument
        print('Hello') #function call, argument, log statement

print_hello_x_or_ten_times() #function call
print_hello_x_or_ten_times(4) #function call, argument


""" multi line comment
Bonus section
"""

# print(num3) #single line comment, NameError
# num3 = 72 #variable declaration, numeric
# fruit[0] = 'cranberry' #TypeError
# print(person['favorite_team']) #KeyError
# print(pizza_toppings[7]) #IndexError
#   print(boolean) #IndentationError 
# fruit.append('raspberry') #AttributeError
# fruit.pop(1) #AttributeError