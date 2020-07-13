# Question: Same Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,p,q):
        if(p==None and q==None):
            return True
        elif(p==None and q!=None):
            return False
        elif(p!=None and q==None):
            return False
        elif(p.val!=q.val):
            return False
        else:
            left = self.check(p.left,q.left)
            right = self.check(p.right,q.right)
            return left and right
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.check(p,q)