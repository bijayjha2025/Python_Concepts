'''
Loops means repeating a block of code until a certain condition is met. In Python, there are two main types of loops: for loops and while loops.
'''

# for loop: we use this to iterate over a sequence (like a list, tuple, string) or other iterable objects. It is used when we know the number of iterations beforehand.

a = 10
for i in range(10):
    print(i)

l = [1, 2, 3, 4, 5]
for i in l:
    print(i * i)

t = (1, 2, 3, 4, 5)
for i in t:
    print(i + i)

s = "Bijay"
for i in s:
    print(i)


d = {"name": "Bijay", "age": 20, "city": "Itahari"}
for i in d:
    print(i, d[i])


#Noticed? In case of list and tuple, we got each element. In case of string, we got each character. In case of dictionary, we got each key and value.

# There is also a unique case of for with else, where else will be executed after the for loop is completed.

l1 = [1,4,6]
for i in l1:
    print(i)
else:
    print("Loop is completed.")


# while loop: we use this to execute a block of code as long as a specified condition is true. It is used when we do not know the number of iterations beforehand.

i = 0
while i < 10:
    print(i)
    i += 1

#In while loop, we need to make sure that the condition will eventually become false, otherwise it will lead to an infinite loop.


i1 = 0
while i1 < 5:
    print(i1)
    i1 += 1


i3 = 5
while i3 > 0:
    print(i3)
    i3 -= 1



#Break and continue statements: In Python, we can use the break statement to exit a loop prematurely, and the continue statement to skip the current iteration and move on to the next one.

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i == 5:
        continue
    print(i)


#For loop with break and continue statements:
for i in range(10):
    if i == 5:
        break
    elif i == 3:
        continue
    print(i)

# The range() function: The range() function is used to generate a sequence of numbers. It can take one, two, or three arguments. If one argument is provided, it generates numbers from 0 to that number (exclusive). If two arguments are provided, it generates numbers from the first argument to the second argument (exclusive). If three arguments are provided, it generates numbers from the first argument to the second argument (exclusive) with a step size of the third argument.

print(list(range(10))) #This will generate numbers from 0 to 9
print(list(range(1, 10))) #This will generate numbers from 1 to 9
print(list(range(1, 10, 2))) #This will generate numbers from 1 to 9 with a step size of 2


#They are used to generate a sequence of numbers, which can be useful in loops and other situations where we need to iterate over a range of values.

#Using range with for loop:
for i in range(5):
    print(i)

#Using range with while loop:
i = 0
while i < 5:
    print(i)
    i += 1

#They are also used in list comprehensions, which are a concise way to create lists in Python.
l = [i for i in range(5)]
print(l)


#Pass statement: The pass statement is a null operation; it does nothing when executed. It is used as a placeholder in situations where a statement is syntactically required but no action is needed. For example, we can use the pass statement in loops, functions, classes, and conditional statements.

for i in range(5):
    pass #This is a placeholder for future code