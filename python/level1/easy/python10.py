'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Ex1
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7
Ex2
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        countMap={}
        longestEven=[]
        longestOdd=[]
        for c in s:
            if c in countMap:
                countMap[c]+=1
            else:
                countMap[c]=1
        for k,v in countMap.items():
            if v%2==0:
                longestEven.append(v)
            else:
                q=v//2
                longestOdd.append(q*2)
        if longestOdd:
            return sum(longestEven)+sum(longestOdd)+1
        else:
            return sum(longestEven)