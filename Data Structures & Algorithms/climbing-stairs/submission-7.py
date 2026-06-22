class Solution:
    def climbStairs(self, n: int) -> int:
        hasmap = {

        }
        def fibSeq(num):
            if num in hasmap:
                return hasmap[num]
            if num <= 0:
                return 0
            if num == 2 or num == 1:
                return num
            hasmap[num] = fibSeq(num-1) + fibSeq(num-2)
            return hasmap[num]
        return fibSeq(n)