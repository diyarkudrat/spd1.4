"""
Problem: Given single linked list, find the middle item. If linked list has an even length, return the two middle items.


Input:  3 -> 6 -> 2 -> 8 ->

Output: 6, 2

Solution:

Find the length of the linked list.
Divide the length by 2.
If remainder return the two middle ones

"""

Class Node(object):

    Def __init__(self, data):
    Self.data = data
    Self.next = None

Class LinkedList(object):

    Def length(self):
    Count = 0
    While self.head is not None:
        Count += 1
    Return count

    Def return_middle_item(self):
    Middle_item, remainder = divmod(LinkedList.length(), 2)


    Curr_node = self.head
    Next_node = curr_node.next
    While curr_node <= middle_item:
        If curr_node == middle_item:
            If remainder == 1:
                Return curr_node
            Else:
                return curr_node + next_node
        Else:
            Curr_node = next_node
            Next_node = next_node.next

            # Divide count by 2
            
            # If remainder = 0, return 2 middle items

            # while loop, curr_node <= middle index

            # If linkedlist is even amount, return the middle index and the one after it.