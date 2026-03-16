# Create the list of first names
studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]

# Print each name with "Evans" using a for loop
print("Original list with last names:")
for name in studentNames:
    print(name + " Evans")

# Ask the user to add another name
new_name = input("\nEnter another first name to add to the list: ")
studentNames.append(new_name)

# Print the updated list with new last names
print("\nUpdated list with last names:")
for name in studentNames:
    print(name + " Evans")
