def countdown(num):
    result = list(range(num, -1, -1))
    return result

countdown(5)

def print_and_return(a_list):
    print(a_list[0])
    return a_list[1]

print_and_return([1,2])

def first_plus_length(a_list):
    return a_list[0] + len(a_list)

first_plus_length([1,2,3,4,5])

def values_greater_than_second(a_list):
    if len(a_list) < 2:
        return False

    result =[]
    second = a_list[1]
    for i in a_list:
        if i > second:
            result.append(i)
    
    print(len(result))
    return result

values_greater_than_second([5,2,3,2,1,4])
values_greater_than_second([3])

def length_and_value(size, value):
    result = [value for i in range(size)]
    return result

length_and_value(4,7)
length_and_value(6,2)