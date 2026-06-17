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