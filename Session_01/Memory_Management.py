# How Memory Management Works in Python?

"""
Python itself manages memory, which means the programmer does not have to worry about allocating and deallocating memory. Python uses two main mechanisms for memory management: reference counting and garbage collection.

1. Garbage Collection:
Python uses a garbage collection mechanism to automatically free up memory that is no longer in use.
a. If an object has no references pointing to it, garbage collector removes it from memory.
b. This ensures that unused memory can be reused for new objects.
c. Python's garbage collector also handles cyclic references, which can occur when two or more objects reference each other, preventing them from being collected.


2. Reference Counting:
Every object in Python keep a reference counter, which tells how many references are currently pointing to that object.
When a new reference is created, counter is incremented.
When a reference is deleted or goes out of scope, counter is decremented.
If counter reaches zero, it means there are no references to the object, and it can be safely deallocated from memory.

"""

a = [1, 2, 3]
b = a

print(id(a), id(b))

if id(a) == id(b):
    print("a and b are referencing the same object in memory.")





#Memory Optimization with small integers
'''

Python applies an internal optimization technique called object interning for small immutable objects (like integers from -5 to 256 and some strings). Instead of creating a new object for each occurrence of the values, Python reuses the same object to save memory.

'''

x = 10
y = 10
#Here Python does not create two separate objects for 10. Instead, it creates one object for 10 and both x and y reference that same object in memory.
print(id(x), id(y))

#Here, both x and y point to the same memory location where the value 10 is stored. This optimization helps reduce memory usage and improve performance when dealing with small integers and certain strings.


#But if we change as,
x= 10
y = x
x +=1

if id(x) != id(y):
    print("x and y are referencing different objects in memory.")
