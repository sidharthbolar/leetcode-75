'''
438. Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        resul t =[]
        windo w =len(p)
        range s =len(s)
        counter_ p =Counter(p)
        if (windo w >ranges):
            return []
        else:
            for index in range(range s -windo w +1):
                if (inde x= =0):
                    counter_ s =Counter(s[index:windo w +index])
                else:
                    counter_s[s[inde x -1] ]- =1
                    counter_s[s[inde x +windo w -1] ]+ =1

                if len(counter_ s -counter_p )= =0:
                    result.append(index)
        return result