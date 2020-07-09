# question : Maximum Width of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if(root == None) : return 0
        max_width = 1
        queue = [[root,1,1]]
        while(len(queue)!=0):
            length = len(queue)
            widths = []
            for i in range(0,length):
                root1 = queue.pop(0)
                if(root1[0].left!=None):
                    widths.append(root1[2]*2)
                    queue.append([root1[0].left,root1[1]+1,root1[2]*2])
                if(root1[0].right!=None):
                    widths.append(root1[2]*2+1)
                    queue.append([root1[0].right,root1[1]+1,root1[2]*2+1])
            
            if(len(widths)>1):
                max_width = max(max_width,max(widths)-min(widths)+1)
        return(max_width)
            
        