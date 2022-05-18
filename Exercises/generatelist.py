# Example provided
# split user input by comma and space ", "

sequence = input("Enter a sequence of numbers: \n") #3, 5, 6, 7, 8

print("List: ", sequence.split(", "))
print("Tuple: ", tuple(int(x) for x in sequence.split(", ")))
