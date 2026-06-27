''' To print the multiplication table of a number entered by the user.
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
'''

num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{num} X {i} = {num * i}")