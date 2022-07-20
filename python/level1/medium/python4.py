'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''

class Solution:

    def dfs(self, grid, i, j):

        m,n= len(grid),len(grid[0])

        #if index out of bound then exit
        if i < 0 or j < 0 or i >= m or j >= n:
            return
        #if water detected then exit
        if grid[i][j] == '0':
            return

        #if water not detected flood the island only across the 4-D
        grid[i][j] = '0'


        self.dfs(grid, i-1, j) #up
        self.dfs(grid, i+1, j) #down
        self.dfs(grid, i, j - 1) #left
        self.dfs(grid, i, j + 1) #right

    def numIslands(self, grid: List[List[str]]) -> int:
            res = 0
            m = len(grid)
            n = len(grid[0])

            i, j = 0 , 0

            for i in range(m):
                for j in range(n):

                    #whenever you find an island, result += 1 and flood it.
                    if grid[i][j] == '1':
                        res += 1
                        self.dfs(grid, i,j)#Once the recursion ends all joined island will be covered as 1 with neighbours flooded

            return res

