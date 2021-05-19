# a.
# *
# **
# ***
# ****
#
# rows = int(input("Please Enter the Total Number of Rows  : "))
#
# print("Right Angled Triangle Star Pattern")
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print('*', end = ' ')
#     print()

# b.
#   *
#  ***
# *****
#  ***
#   *
# h = eval(input("please enter diamond's height:"))
# for i in range(h):
#     print(" "*(h-i), "*"*(i*2+1))
# for i in range(h-2, -1, -1):
#     print(" "*(h-i), "*"*(i*2+1))

# c.
# 1010101
# 10101
# 101
# 1
N= 5
k = 2 * N - 2
# Outer loop in reverse order
for i in range(N, -1, -1):
    # Inner loop will print the number of space.
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    # This inner loop will print the number o stars
    for j in range(0, i + 1):
        print(j%2, end=" ")
    print("")

