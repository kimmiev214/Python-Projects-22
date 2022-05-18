# Test sequence of numbers for uniqueness

sequence = input("Enter a sequence of numbers: \n") #3, 5, 6, 7, 8
values = sequence.split(", ")

def are_different(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False

values_list = []
for x in values:
    values_list.append(int(x))

print(are_different(values_list))






