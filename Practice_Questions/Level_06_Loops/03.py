'''
Use nested loops to print the following pattern:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
'''

for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()
