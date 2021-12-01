#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#Will show a 5 on the console

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#This will produce a traceback as the function number_of_days_in_a_week_silicon_or_triangle_sides has not been defined with no parameters in this file nor given any defaults to fall back on

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#Will show a 5 on the console as the first return statement will exit out of the function block before the second return statement will ever be looked at

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#Same as number 3, the return function will exit out before the print function is able to be called

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#Will show 5 on the console as 'x' has been assigned the value 5 from the function.

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#Will show 8 on the console, the function calls effects the equation (1+3) + (2+3)

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#Will show 25 on the console as the arguments given to the function are converterted to ther string representations and then concatenated together

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#Will show 100 on one line and 10 on a second line of the console

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#Will show 7, 14, 21 on three separate lines in the console

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#Will show 8 on the console

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#Will show 500, 500, 300, 500 on separate lines in the console

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#Will show 500, 500, 300, 300, 500 on separate lines of the console

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#Will show 500, 500, 300, 300, 300 on separate lines of the console


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#Will show 1, 3, 2 on separate lines of the console

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#Will show 1, 3, 5, 10 on separate lines of the console