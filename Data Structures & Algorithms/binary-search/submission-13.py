class Solution:

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        mid = (r + l) // 2
        while True: 
            prev_mid = mid 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: 
                l = mid 
                mid = (r + l) // 2
            elif nums[mid] > target:
                r = mid
                mid = (r + l) // 2
            else:
                return -1
            
            if prev_mid == mid:
                return -1

