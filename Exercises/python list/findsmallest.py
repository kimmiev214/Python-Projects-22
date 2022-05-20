# Take user input of a list and then find the smallest element

heights = []

n = int(input("Enter number of elements: "))

for i in range(0, n):
    ele = int(input())
    heights.append(ele) # add element to heights

smallest_number = heights[0]

for number in heights:
    if number < smallest_number:
        smallest_number = number


print(smallest_number)