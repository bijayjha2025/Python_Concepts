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