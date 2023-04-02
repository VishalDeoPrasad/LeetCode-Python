class Solution(object):
    def islandPerimeter(self, grid):
        row = len(grid)
        col = len(grid[0])
        cnt = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    if grid[i-1][j] == 0 or i-1<0:          #up
                        cnt += 1
                    if i+1 >= row or grid[i+1][j] == 0:     #down
                        cnt += 1
                    if grid[i][j-1] == 0 or j-1<0:          #left
                        cnt += 1
                    if j+1 >= col or grid[i][j+1] == 0:     #right
                        cnt += 1
        return cnt
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(Solution().islandPerimeter(grid))