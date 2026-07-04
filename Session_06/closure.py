'''Python Closures: In Python, a closure is a function object that has access to variables in its enclosing lexical scope, even after the outer function has finished executing. Closures are often used to create functions with private data or to maintain state between function calls.

'''
def addTen(x):
    ten = 10

    def add(y):
        return y + ten + x
    return add

closureResult = addTen(5)
print(closureResult(3))
print(closureResult(7))

#Here addTen is outer function with x as paramter and add is inner function with y. Inside add, we are accessing ten though it is defined in outer function. When we call addTen(5), it returns the inner function add with x=5 and ten=10. When we call closureResult(3), it adds 3 + 10 + 5 = 18. Similarly, closureResult(7) adds 7 + 10 + 5 = 22. This demonstrates how closures can maintain state and access variables from their enclosing scope even after the outer function has completed execution.


#Another example:

def outerFunction(msg):
    message = msg

    def innerFunction():
        print(message)

    return innerFunction

result = outerFunction("Hello, world!")
result()