# 1. Restate Question

    # Given array, write a function that executes n left rotations on the array

    # Given: [5,6,7,8,9]

    # Output: [6,7,8,9,5]

# 2. Ask Clarifying Questions

    # Will the number of rotations be greater than the length of the array?
    # What types are the inputs?
    # Should I return a new list?
    # Can I use built-in functions or a library?

# 3. State your assumptions

    # Input is not sorted
    # Every value in list is the same type
    # Return a new list

# 4. Think out loud

    # a. Brainstorm solutions
        # Create temporary array with n numbers
        # Shift the remaining numbers
        # Add temporary array back
        
        # Another solution: Linked List!

    
arr = [1, 2, 3, 4, 5 , 6]

def left_rotate(arr, n):  # n = input of number of rotations

    temp_array = []
    for i in range(arr[n - 1]):
        temp_array.append(i)

        for j in range(0, len(arr) - n):
            arr[j] = arr[j + 1]
    
    arr.append(temp_array);

    # print(temp_array)
    print(arr)



left_rotate(arr, 4)

