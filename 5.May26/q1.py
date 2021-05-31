# Q.No.1
def ascii_sum(s):
    for i in range(len(s)+1):
        total = []
        for j in range(i):
            total.insert(j,ord(s[j]))
    total_sum = sum(total)
    return total_sum
def ascii_sum_odd(s):
    for i in range(len(s)+1):
        odd = []
        for j in range(i):
            if j  % 2 == 0:
                odd.insert(j,ord(s[j]))
    odd_sum = sum(odd)
    return odd_sum
def ascii_sum_even(s):
    for i in range(len(s)+1):
        even = []
        for j in range(i):
            if j % 2 != 0:
                even.insert(j,ord(s[j]))
    even_sum = sum(even)
    return even_sum

s = input("Enter a string: ")
print("Total ASCII Sum: ",ascii_sum(s))
print("ASCII Sum of odd-numbered characters: ",ascii_sum_odd(s))
print("ASCII Sum of even-numbered characters: ",ascii_sum_even(s))