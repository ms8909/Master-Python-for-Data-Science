# Q.No.2
def get_bool(prompt):
    while True:
        try:
           return {"true":True,"false":False}[input(prompt).lower()]
        except KeyError:
           print ("Invalid input please enter True or False!")

user_first_input = get_bool("Enter 'True' or 'False': ")
user_second_input = get_bool("Enter 'True' or 'False': ")

if user_first_input ==False and user_second_input==False:
    print("XOR Result: ", False)
elif user_first_input ==True and user_second_input==False:
    print("XOR Result: ", True)
elif user_first_input ==False and user_second_input==True:
    print("XOR Result: ", True)
elif user_first_input ==True and user_second_input==True:
    print("XOR Result: ", False)

