# Write a Python program which accepts the user's first and last name
# and print them in reverse order with a space between them.
#
# User input for first and last name
# Store names into a list
# reverse the array/list
# map() method and convert each item of the list to a string.
# join() method creates and returns a new string by concatenating all the elements in the list

first_name = input("Enter your first name: \n")
last_name = input("Enter your last name: \n")

names = [first_name,  last_name]
names.reverse()

print(' '.join(map(str, names)))