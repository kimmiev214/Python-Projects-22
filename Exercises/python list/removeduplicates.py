# Write a Python program to remove duplicates from a list
if __name__ == '__main__':

    str = ['abb', 'xyz', 'xyz' ,'aba', '1221', 'abb']

    visited = set()
    # Can use visited.add(x) to add to a duplicates set
    dup = [x for x in str if x in visited or (str.remove(x) or False)]
    print(str)

