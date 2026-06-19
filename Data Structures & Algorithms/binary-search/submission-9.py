class Solution:

    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        l = 0
        r = len(nums)
        counter = 0
        while counter < len(nums): 
            print(mid)
            print(nums[mid])
            prev_mid = mid 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: 
                l = mid 
                mid = (r + l) // 2
                print(f'new mid target higher {mid}')
            elif nums[mid] > target:
                r = mid
                mid = (r + l) // 2
                print(f'new mid target lower {mid}')
            else:
                return -1
            
            if prev_mid == mid:
                return -1

            counter += 1

