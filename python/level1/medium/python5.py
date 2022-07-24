'''
Unique Paths
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.
Input: m = 3, n = 7
Output: 28

Ex2
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
'''


# Define Base Class
# Define State
# Define Relation b/w current state and previous state
# Formulate inital recursion solution
# Add Memonization or Tabulation to convert to DP and Voila :)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # base class
        if not m or not n:
            return 0
        dp = [[1 for _ in range(n)] for _ in range(m)]

        # state[uniquepaths of i,j] = state[uniquepaths of i,j-1 + i-1,j]
        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]