# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(curr, maxA):
            if not curr:
                return 0
            res = 1 if curr.val >= maxA else 0
            maxA = max(curr.val, maxA)
            res += dfs(curr.left, maxA)
            res += dfs(curr.right, maxA)
            return res
        return dfs(root, root.val)
