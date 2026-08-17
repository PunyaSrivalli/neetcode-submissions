class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols  = len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        max_area = 0

        def bfs(r,c):
            q = deque()
            area = 1
            grid[r][c] = 0
            q.append((r,c))
            
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0:
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    area += 1
            return area
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    print(grid[i][j])
                    area = bfs(i,j)
                    print(max_area, area)
                    max_area = max(max_area, area) 
        return max_area