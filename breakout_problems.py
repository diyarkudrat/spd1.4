"""
Problem: Given single linked list, find the middle item. If linked list has an even length, return the two middle items.


Input:  3 -> 6 -> 2 -> 8 ->

Output: 6, 2

Solution:

- Find the length of the linked list.
- Divide the length by 2 to find the middle item
- iterate through linked list until you reach the middle item
- If remainder equals 1, return middle item
- If remainder equals 0, return current node and the next node



"""

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):

    def __init__(self, items=None):

        self.head = None
        self.tail = None
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def length(self):
        count = 0
        while self.head is not None:
            count += 1
        return count

    def return_middle_item(self, length):
        """ Time Complexity: O(n) because you are iterating through linked list with n-amount of items
            Space Complexity: 0(n) because linkedlist has n-amount of items

        """

        middle_item, remainder = divmod(length, 2)  # Divide the length of linked list by 2 to get the middle index

        curr_node = self.head  # initial variable to keep track of node at each iteration

        while curr_node is not None:  # Iterate through linked list starting at head node

            if curr_node == middle_item:    # if current node is at the middle index
                if remainder == 1:          # if the linked list's length is an odd number
                    return curr_node        # return the node
                else:
                    next_node = curr_node.next         # if linked list is even amount, return curr_node and the node after
                    return curr_node + next_node
            else:
                curr_node = curr_node.next