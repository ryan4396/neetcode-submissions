class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        freq = [[] for _ in range(len(nums)+1)]
        for num1 in nums:
            if num1 in dic:
                dic[num1] += 1
            else:
                dic[num1] = 1
        for num, cnt in dic.items():
            freq[cnt].append(num)
        result = []
        print(freq)
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                result.append(num)
                print(f'here {result}')
                if len(result) == k:
                    return result