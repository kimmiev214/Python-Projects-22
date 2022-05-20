# Read the problem more clearly next time
# Program asked to compare the characters in the word
# Not compare the strings within the list

# Count the number of strings where the length is 2 or more
# and the first and last character are the same


str = ['abc', 'xyz', 'aba', '1221']

result = 0

for str_ in str:
    if len(str_) > 1 and str_[0] == str_[-1]:
        result += 1;

print(result)



