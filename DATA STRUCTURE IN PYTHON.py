# Data structures in python

# Topic :List
# Exercise
# Q1. Create a list of 5 random numbers and print the list.

list_A = [10, 25, 37, 42, 58]
print("List of 5 numbers:", list_A)

# Q2. Insert 3 new values to the list and print the updated list.
print("list_A=",list_A)
# Insert 3 new values
list_A.extend([70, 80, 90])

# Print the updated list
print("Updated list:", list_A)

# Q3. Try to use a for loop to print each element in the list.
print("Elements in the updated list:")
for number in list_A:
    print(number)

# Topic: Dictionary
# Exercise
# Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.

Details = {
    'name': 'John',
    'age': 25,
    'address': 'New York'
}

# Print the dictionary
print("Details:", Details)

# Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'.

Details['phone'] = '1234567890'

print("Updated Details:", Details)

# Topic: Set
# Exercise
# Q1.Create a set with values 1, 2, 3, 4, and 5.

Set_A = {1, 2, 3, 4, 5}

print("Set_A:", Set_A)

# Q2. Add the value 6 to the set created in Q1.

# Adding the value 6 to the set
Set_A.add(6)

# Display the updated set
print("updated set=",Set_A)

# Q3. Remove the value 3 from the set created in Q1.

# Removing the value 3 from the set
Set_A.remove(3)

# Display the updated set
print("Updated set=",Set_A)

# Topic:Tuple
# Exercise
# Q1. Create a tuple with values 1, 2, 3, and 4
tuple_A = (1, 2, 3, 4)

# Display the tuple
print("tuple=",tuple_A)

# Q2. Print the length of the tuple created in Q1.
print("tuple=",tuple_A)
print(len(tuple_A))
