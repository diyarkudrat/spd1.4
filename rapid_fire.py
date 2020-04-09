# Input = ['a', 'b', 'c']
#         ['c', 'b', 'a', 'a']

# Output = True 

# Solution #1: Double loop

# Solution #2: Create first as a histogram. Loop through the second array
#               and add one to the count. If all counts of histogram is the same value,
                # return True, otherwise return False.




# Given a sorted array and element, return the 
# first and last index occurence of that given element, otherwise if given element
# isn't in array, return None

# Input = ['a', 'b', 'a', 'd', 'e'] // Given element = a
# Output = [0, 2]

# Solution #1: For loop 
        # For each element in array, check if element is == to the given element.
            # If it is equal, add its index to new list. If not in array, return None. 
            # At the end , return the first and last index of the list of indexes.

# Input = ['a', 'b', 'a', 'd', 'e', 'a'] // Given element = a
                                    


