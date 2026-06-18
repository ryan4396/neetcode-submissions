class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = set([i for i in s])
        counters = {}
        bool_val = True
        if len(s) == len(t):
            for i in letters:
                counters[i] = s.count(i)
            for e in t:
                if e in letters and counters[e] > 0:
                    counters[e] -= 1
                else:
                    bool_val = False
        else:
            bool_val = False
        return bool_val