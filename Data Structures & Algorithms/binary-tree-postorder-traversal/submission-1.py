# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       stack, res=[],[]
       curr=root
       last_visited = None
       while curr or stack:
        if curr:
            stack.append(curr)
            curr=curr.left
        else:
            peek_node=stack[-1]

            if peek_node.right and last_visited != peek_node.right:  
                curr = peek_node.right
            else:
                res.append(peek_node.val)
                last_visited = stack.pop()    
       return res 
