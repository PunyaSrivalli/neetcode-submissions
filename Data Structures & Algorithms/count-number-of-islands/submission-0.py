class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        Rows = len(grid)
        Cols = len(grid[0])
        islands = 0

        def bfs(r,c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr,dc in directions:
                    nr, nc = row+dr, col+dc
                    if (nr < 0 or nc < 0 or nr >= Rows or nc >= Cols or grid[nr][nc] == "0"):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"



        for i in range(Rows):
            for j in range(Cols):
                if grid[i][j] == "1":
                    bfs(i,j)
                    islands += 1
        return islands