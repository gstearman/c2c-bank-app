# 1. Note the variable login_types, the list of account types.
login_types = ["admin", "user", "guest"]
# 2. Complete the function called gatekeeper that returns the following error message strings in the following scenarios:
# For “admin”:
# program says “You have the privileges.”
# For “user”:
# program says “You have limited privileges.”
# For “guest”:
# program says “You have no privileges.”
def gatekeeper(login):
  if login == "admin":
    return "You have the privileges."
  elif login == "user":
    return "You have limited privileges."
  elif login == "guest":
    return "You have no privileges."
  else:
    return "Illegal login type!"

# 3. Call the gatekeeper function with a string and print what it returns.
print("For \"admin\" gatekeeper returns: \n" + gatekeeper("admin")+"\n")
print("For \"user\" gatekeeper returns: \n" + gatekeeper("user")+"\n")
print("For \"guest\" gatekeeper returns: \n" + gatekeeper("guest")+"\n")
print("For \"blashblahblah\" gatekeeper returns: \n" + gatekeeper("blahblahblah")+"\n")

# 4. How could this code be improved? Make it better. Think about what other scenarios you should cover in your if logic.
# Error checking for illegal login type
# Print statements that show the input and output from login

# 5. Complete the function called check_balance that takes one parameter, loan_balance.
def check_balance(loan_balance):
# 6. If loan_balance is zero or more, it says “you don’t owe any money”
# 7. If loan_balance is negative, it  says “you owe $X” where X is the amount
  if loan_balance >= 0:
     return "You don't owe any money."
  else:
     return "You owe $"+str(abs(loan_balance))+".\n"


# 8. Call your function with a negative and positive number and print what it returns.
print("check_balance(300) returns: \n" + check_balance(300)+"\n")
print("check_balance(-300) returns: \n" + check_balance(-300)+"\n")
print("check_balance(-300.55) returns: \n" + check_balance(-300.55)+"\n")

