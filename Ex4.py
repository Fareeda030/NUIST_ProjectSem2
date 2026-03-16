#Ask for user's age

age = int(input("Enter your age:"))

#Using if condition
if age <= 19:
  print("You qualify for student discounts.")
elif age<55:
  print("You qualify for no age discounts.")
else:
  print("You can receive senior discounts.")

