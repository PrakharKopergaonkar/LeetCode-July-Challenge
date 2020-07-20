# Question : Remove Linked List Element

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        Dummy = ListNode()
        Dummy.next = head 
        a = Dummy
        while(a!=None):
            if(a.next!=None and a.next.val==val):
                a.next = a.next.next
            else:
                a = a.next
                
        return Dummy.next