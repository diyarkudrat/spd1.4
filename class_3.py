# Problem: Find the 5th largest value in an array of numbers

# Restate the problem: Given array of numbers, return 5th largest value

# Ask clarifying questions: Are the numbers integers or floats? Is the array sorted? 

# State assumptions: Numbers are integers. Assuming the array is unsorted

# Example Input: [1, 3, 7, 14, 6, 9, 12]

# Output: 9

# Possible Solutions:

        # 1. Sort array:

            # Sort numbers
            # Return 5th element

        # 2. Min-heap data structure:


Problem: Given an array a of numbers and a target value t, find two numbers that sum to t (that is, a[i] + a[j] = t).

# Input: [2, 4, 5, 7]  sum = 7

# Output: [2, 5]

# Solution #1:

        # Double for loop
        # One loop keeps track of the initial index and another loop keeps check of the index after.
        # Loop through the array and check if the two indexes equal each other

# Solution #2:

        # Create hash set. Keeping track of the complmentary number for each number in array.
        # [2, 4, 5, 7]
        # Loop through array
        # for each index in array, check if its cimplementary is in the set. 
        # If it is, return the index you're at its complemtary.
        # otherwise, add the complementary to the hash set.

        def two_sum_numbers(arr, sum_val):
            complementary_nums = set()


            for i in arr: # 0(n)
               comple = sum_val - i             # Subtract the index you're at with the sum that's given.
               if comple is in complementary_nums:
                   return i + comple
                else:
                    # add comple to hash set


Problem: Given 2 arrays of n numbers each, find a pair of numbers (one from each array) whose sum is closest to a given target value t.


# Input: [2, 5, 3, 1]  [4, 3, 7, 2]  sum = 11

# Output: [5, 7]  sum is 12 however it's pretty close to the target sum

# Naive Solution:

        # double for loop
        # loop through each array and check if the indexes add up to 11 or is close to 11

# Better Solution:

        # Implement hash set
        # Hash set one of the arrays for constant lookup time
        # Loop through other array and check if its complementary number is in hash set
        # If not, use recursion and either add or subtract one from target sum


# Problem: Reverse given linked list reusing its original nodes

# Input: 3 -> 7 -> 1 -> 8 -> 

# Output: 8 -> 1 -> 7 -> 3 ->

# Solution:
    
    # Reverse each pointer in linked list
    # Switch up the head and tail nodes

    class Node(object):

        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList(object):

        def reverse(self):
            
            prev_node = None
            current_node = self.head
            next_node = current_node.next

            while current_node is not None:    # loop through linked list  0(n)

                current_node.next = prev_node
                prev_node = current_node
                current_node = next_node
                next_node = next_node.next

            holder = self.head
            self.head = self.tail
            self.tail = holder
            













     


