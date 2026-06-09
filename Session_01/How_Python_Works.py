
#How Python Works?

"""
Compared to other languages, there is a vast difference in working of Python.

Python does not convert the code into machine code directly. Instead it converts the code into something called bytecode (.pyc or .pyo files) and since this bytecode cannot be understood by the machine, Python uses an Interpreter called Python Virtual Machine (PVM ) to execute bytecodes.

Let's understand the complete order of things that happen when we run a Python program.
1. First, we write the code in a Code Editor and then save it with a .py extension. The saved file is called a Python Source Code or Source File.
2. When we run the program, the Compiler in Python Interpreter plays its role and converts the source code into bytecode (.pyc or .pyo files). This bytecode is a low-level representation of the source code and is not human-readable.
3. The bytecode is then sent to the Python Virtual Machine (PVM), which is an interpreter that executes the bytecode. The PVM reads the bytecode and executes it line by line, translating it into machine code that can be understood by the computer's hardware. Finally, the output is generated.


"""