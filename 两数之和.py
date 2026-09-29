class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        cache = {}
        ans = []
        for i , items in enumerate(nums):
            other_target = target - items 
            if other_target in cache:
                ans = [i,cache[other_target]]
            else:
                cache[items] = i
        return ans