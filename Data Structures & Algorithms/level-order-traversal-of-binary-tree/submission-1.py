# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)
        while q:
            l = []
            lenq = len(q)
            for i in range(lenq):
                ele = q.popleft()
                
                if ele:
                    l.append(ele.val)
                    q.append(ele.left)
                    q.append(ele.right)
            if l:
                res.append(l)
        return res
                