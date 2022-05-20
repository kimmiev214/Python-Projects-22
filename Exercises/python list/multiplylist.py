# Write a Python program to multiply all the items in a list.
# Using traversal of list to multiply elements.

list = [10, 100, 1000]
list_two = [3, 6, 9, 12]
list_three = [20, 50, 150, 200, 250]

def multipy_list(list):
    result = 1
    for x in list:
        result = result * x
    return result

print(multipy_list(list))
print(multipy_list(list_two))
print(multipy_list(list_three))



