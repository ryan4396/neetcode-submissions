class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list1 = {}
        for i in range(len(nums)):
           if (target - nums[i]) in list1:
                return sorted([i, list1[target-nums[i]]])
           list1[nums[i]] = i