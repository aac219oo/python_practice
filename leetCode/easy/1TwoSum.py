'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

from typing import List #為了讓List[int]符合規則才加上去的

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): #在歷遍一次，並且i+1避免重複值相加
                num1 = nums[i]
                num2 = nums[j]
                if target == num1 + num2:
                    return [i, j]
        return[] #沒有答案時回傳空陣列
    
print(Solution().twoSum([2,1,6], 9))