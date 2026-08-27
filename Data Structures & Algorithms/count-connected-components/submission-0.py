class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preM = {i:[] for i in range(n)}
        for s,d in edges:
            preM[s].append(d)
            preM[d].append(s)
        visited = set()
        count = 0
        def dfs(node):
            if node in visited:
                return True
            visited.add(node)
            for d in preM[node]:
                dfs(d)
            return False


        for i in range(n):
            if not dfs(i):
                count += 1
        return count