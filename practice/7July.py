name1= "Tazeen"
gender= "f"
dob="1990"

#deposit 100
def deposit(deposit_amount, balance):
    new_balance= balance+ deposit_amount
    return new_balance

deposit_amount= int(input("How much amount to deposit?"))

balance= deposit(deposit_amount, balance)
print("this is new balance :",balance)

#withdraw
def withdraw(w_amount,balance):
    if balance<w_amount:
        print("This is not possible")
        return balance
    else:
        new_balance = balance-w_amount
        return new_balance

w_amount = int(input("How much do you want to withdraw?"))

print(w_amount)