class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {num: 0 for num in nums}
        for i in nums:
            dic[i] += 1
        sorted_keys = sorted(dic, key=dic.get, reverse=True)
        return sorted_keys[:k]