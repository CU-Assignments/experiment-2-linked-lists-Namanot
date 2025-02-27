# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None or head.next is None:
            return
        else: 
            length = 0
            temp = head
            while temp:
                length += 1
                temp = temp.next
            middle_index = length // 2
        
            temp = head
            prev = None
            for i in range(middle_index):
                prev = temp
                temp = temp.next           
            if prev:
                prev.next = temp.next            
            return head

        