
tuple1 = () #This is an empty tuple
print(tuple1, type(tuple1))

tuple2 = ("Okay", "Haha", "Hello", "World")
tuple3 = ("Thanks", "Bye", "See you")

#Join two tuples
tuple4 = tuple2 + tuple3
print(tuple4)

print(len(tuple4)) #Length of the tuple

#Modify the tuple and add more members and assign it to a new tuple
tuple5 = tuple4 + ("Python", "Java", "C++")
print(tuple5)


#Unpacking tuple with other words and programming languages
(a, b, c, d) = tuple2
print("Unpacking tuple2 with other words and programming languages:")
print(f"a = {a}, b = {b}, c = {c}, d = {d}")

