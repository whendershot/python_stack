for i in range(1, 151):
    print(i)

for i in range(5, 1001, 5):
    print(i)

for i in range(1, 101, 1):
    if (i % 10 == 0):
        print("Coding Dojo")
    elif (i % 5 == 0):
        print("Coding")
    else:
        print(i)

sum = 0;
for i in range(1, 500001, 2):
    sum += i
print(sum)

for i in range(2018, -1, -4):
    print(i)

lowNum = 2
highNum = 55
mult = 3
for i in range(lowNum, highNum + 1):
    if (i % mult == 0):
        print(i)