heights = [100, 1000, 2540, 2200, 200, 500]

largest_number = heights[0]

for number in heights:
    if number > largest_number:
        largest_number = number

print(largest_number)