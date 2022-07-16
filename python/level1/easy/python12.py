'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Ex1:Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Ex2:Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        resul t =0

        while nums:
            len_spli t =int(len(nums ) /2)
            if (len_spli t= =0 ) &(targe t= =nums[len_split]):
                return result
            eli f((len_spli t= =0 ) &(targe t! =nums[len_split])) :
                return -1
            else:

                if (targe t >nums[0:len_split][-1]):
                    num s =nums[len_split:]
                    resul t+ =len_split
                else:
                    num s =nums[0:len_split]

        return result


