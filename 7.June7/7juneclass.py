# #data types
# 1. int
# 2. float
# 3. Strings 
# 4. boolean

# # data strucutes
# 1. list/array
# 2. tuple
# 3. dictionaries


# # Special structues 
# 1. if-else
# 2. loops
# 3. functions
# 4. recursion

# # Algorithms
# 1. bubble sort
# 2. selection sort
# 3. linear search


def printsomething(counter):
    print("start", counter)

    counter= counter +1
    if counter<4:
        printsomething(counter)

    print("end ", counter)

    

counter= 0
printsomething(counter)


# function 0
#     start 0
#     counter = counter + 1
#     function 1
#         start 1
#         function 2
#             start 2
#             function 3
#                 start 3
#                 end 4
#             end function 3
#             end 3
#         end function 2

#         end 2
#     end function 1

#     end 1


4!= 4*3*2*1
5!= 5*4*3*2*1   === 1*2*3*4*5

fictorial_of= 5
product= 1

for i in range(1,fictorial_of+1): 
    product= product*i


5!= 5*4*3*2*1*1

5! = 5*24









0! = 1

def fic(number):

    if number>0:
        product= number* fic(number -1 )
        return product
    else:
        return 1



