'''
424. Longest Repeating Character Replacement
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''

# TODO Review Solution

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## RC ##
        ## APPROACH : SLIDING WINDOW ##
        # Logic #
        # 1. Increase the window if the substring is valid else,
        # 2. slide the window with the same length. No need to shrink the window

        ## TIME COMPLEXITY : O(N) ##
        ## SPACE COMPLEXITY : O(N) ##

        freqDict = defaultdict(int)
        maxFreq = 0
        maxLength = 0
        start = end = 0
        while end < len(s):
            freqDict[s[end]] += 1

            # maxFreq may be invalid at some points, but this doesn't matter
            # maxFreq will only store the maxFreq reached till now
            maxFreq = max(maxFreq, freqDict[s[end]])

            # maintain the substring length and slide the window if the substring is invalid
            if ((end - start + 1) - maxFreq) > k:
                freqDict[s[start]] -= 1
                start += 1
            else:
                maxLength = max(maxLength, end - start + 1)
            end += 1
        return maxLength