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



"""
Problem: Given a string of text and a number k, find the k words in the given text that appear most frequently. 
            Return the words in a new array sorted in decreasing order.

Input: "hello there hello world hello there" k=2

Output: ['there', 'hello']

Solution:
    - sort out each word in string
    - create empty dictionary (key, value) = (word, count)
    - Sort keys based on count in descending order and add to new array
    - based on k, add the k amount of words into new array

"""

def frequent_k_words(str, k):
    list_of_words = str.split()
    
    new_dict = {}
    for word in list_of_words:
        if word not in new_dict:
            new_dict[word] = 1
        else:
            new_dict[word] += 1

    list_of_keys = sorted(new_dict.items(), key=lambda item: item[1])

    print(list_of_keys)

    return list_of_keys[k+1::]



str = "there hello hello world hello there diyar kudrat"

print(frequent_k_words(str, 2))