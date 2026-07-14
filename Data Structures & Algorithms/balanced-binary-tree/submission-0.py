# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        curr = root
        self.res = True
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            
            if left - right > 1 or right - left > 1:
                self.res = False
            return 1 + max(left, right)
        dfs(curr)
        return self.res  


            
