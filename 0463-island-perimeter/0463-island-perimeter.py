class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri = 0
        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:

                    #t
                    if r== 0 or grid[r-1][c] == 0:
                        peri +=1
                    #b
                    if r== row-1 or grid[r+1][c] == 0:
                        peri +=1
                    #l
                    if c== 0 or grid[r][c-1] == 0:
                        peri +=1
                    #r
                    if  c== col-1 or grid[r][c+1] == 0:
                        peri +=1
        return peri
