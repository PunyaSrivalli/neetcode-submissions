class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid == [[0]]:
            return 0
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()
        fresh = 0
        rotten = 0
        
        def rot(r,c):
            nonlocal fresh
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1  or (r,c) in visit:
                return 
            visit.add((r,c))
            q.append((r,c))
            fresh -= 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        rotten = len(q)
        mins = 0
        while q and fresh > 0:
            mins += 1
            for i in range(len(q)):
                r,c = q.popleft()
                print(r,c,mins)
                rot(r-1,c)
                rot(r+1,c)
                rot(r,c-1)
                rot(r,c+1)
            
        
        if fresh > 0:
            return -1
        return mins
            
            