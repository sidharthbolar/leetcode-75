'''
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

#On2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numLength = len(nums)
        for i in range(0, numLength):
            for j in range(i + 1, numLength):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
#On
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            if n in dic:
                return [dic[n], i] # case when match is found!
            dic[target-n] = i # add what you need for the given element