 
customer_name = input("Enter customer name: ")

balance = float(input("Enter initial account balance: "))

print("\nInitial Balance:", balance)

deposit = float(input("Enter amount to deposit: "))
balance = balance + deposit

print("Balance after deposit:", balance)

withdraw = float(input("Enter amount to withdraw: "))

if balance - withdraw >= 1000:
    balance = balance - withdraw
    print("Withdrawal successful!")
else:
    print("Withdrawal denied! Minimum balance of 1000 must be maintained.")

print("\n----- Account Details -----")
print("Customer Name:", customer_name)
print("Final Account Balance:", balance)
