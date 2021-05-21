#Calculating Average and Product

#num = 1
print("Enter your entries for Average and its product  ~ Enter ""q"" for Quit")
i=0
store =  []
while i <1:        
        storing_input =  input()
        if storing_input != "q":
            store.append(int(storing_input))

        else:      
           break
i += 1

print("Your entered data : ")
print(store)
#For Average
#used sum function for addition and len function number of values and prints the average
print ("Your average is: ",sum(store)/ len (store))

# For Product
product = 1
for x in store:
    product = product * x
print("Your product is : ", product)