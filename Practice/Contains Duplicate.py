from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        i = 1
        sorted_nums = sorted(nums)
        while i < len(sorted_nums):
            if sorted_nums[i-1] == sorted_nums[i]:
                return True
            else:
                i += 1
        if i == len(sorted_nums):
            return False

s = Solution()
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))