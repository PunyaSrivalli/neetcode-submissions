class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        preM = {i:[] for i in range(n)}
        visited = set()
        for s,d in edges:
            preM[s].append(d)
            preM[d].append(s)
        def dfs(node,parent):
            if node in visited:
                return False
            visited.add(node)
            for d in preM[node]:
                if d == parent:
                    continue
                
                if not dfs(d,node):
                    return False
            return True
        
        if not dfs(0,-1):
            return False
        print(visited)
        if len(visited) != n:
            return False
        return True

                