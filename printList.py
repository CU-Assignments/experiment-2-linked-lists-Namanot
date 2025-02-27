#Your task is to complete this function
#Your function should print the data in one line only

'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    # Function to display the elements of a linked list in same line
    def printList(self, head):
        if head == None:
            return
        else:
            print(head.data, end= " ")
            while head.next:
                head = head.next
                print(head.data,end=" ")
            
        return