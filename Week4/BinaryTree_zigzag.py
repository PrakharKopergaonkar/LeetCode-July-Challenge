# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        count = 0 
        output_list = []
        if(root==None) : return root
        while(len(queue)>0):
            length = len(queue)
            temp_list = []
            for i in range(0,length):
                root = queue.pop(0)
                temp_list.append(root.val)
                if(root.left!=None):
                    queue.append(root.left)
                if(root.right!=None):
                    queue.append(root.right)
            if(count%2==0):
                output_list.append(temp_list)
            else:
                output_list.append(temp_list[::-1])
            count+=1
        
        return output_list