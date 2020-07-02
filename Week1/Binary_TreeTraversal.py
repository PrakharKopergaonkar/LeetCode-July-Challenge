# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        output_list = []
        queue = []
        if(root == None) : return root
        queue.append(root)
        while(len(queue)!=0):
            size = len(queue)
            temp_list = []
            for i in range(size):
                root = queue.pop(0)
                temp_list.append(root.val)
                if(root.left!=None):
                    queue.append(root.left)
                
                if(root.right!=None):
                    queue.append(root.right)
            
            output_list.insert(0,temp_list)
        return output_list
 