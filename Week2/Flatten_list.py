
# Question 10 : Flatten a Multilevel Doubly Linked List
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if(head==None) : return head
        dummy = Node()
        dummy.next = head
        a = head
        stack = [None]
        while(a!=None):
            if(a.next==None and a.child==None):
                    temp = stack.pop()
                    if(temp!=None):
                        temp.prev = a
                    a.next = temp
                    a = a.next
            elif(a.child==None):
                a = a.next
            
            elif(a.next==None):
                temp = a.child
                a.child = None
                a.next = temp
                temp.prev = a
                a = a.next
            else:
                stack.append(a.next)
                temp = a.child
                temp.prev = a
                a.next = temp
                a.child = None
                a = a.next
                
        return dummy.next