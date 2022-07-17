'''
First Bad Version --- Binary Search
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
Ex1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Ex2:
Input: n = 1, bad = 1
Output: 1
'''

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
"""
Input : Int
Output : n
Axiom : isBadVersion(0 to n) will be True for atleast 1 value
Assumption : n>0, 

Approach : Binary Search
BigO : T -> O(Log(n))
"""


class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        bad_version = n
        while start <= end:
            mid = (start + end) // 2
            v = isBadVersion(mid)
            if v:
                bad_version = mid
                end = mid - 1
            else:
                start = mid + 1
        return bad_version

