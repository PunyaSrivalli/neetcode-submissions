# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        cnt = 0
        ele = None
        def inorder(root,k):
            nonlocal cnt
            nonlocal ele
            if not root:
                return
            inorder(root.left,k)
            
            cnt += 1
            if cnt == k:
                ele = root.val
            inorder(root.right,k)
        inorder(root,k)
        
        return ele
