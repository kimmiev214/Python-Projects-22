# Write a Python program to remove and print every third number
# from a list of numbers until the list becomes empty.

numbers_list = [3, 5, 6, 7, 8, 10, 10, 8, 11, 4, 6, 7, 7]
numbers_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in numbers_list:
    print(numbers_list[3-1::3])
    del numbers_list[3-1::3]

print("\n")
for x in numbers_lists:
    print(numbers_lists[3-1::3])
    del numbers_lists[3-1::3]

