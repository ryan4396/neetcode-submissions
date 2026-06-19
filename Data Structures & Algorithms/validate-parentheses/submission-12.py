class Solution:
    def isValid(self, s: str) -> bool:
        boolean = True
        hashmapu = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        not_hasmapu = {
            ")":"(",
            "}":"{",
            "]":"["

        }
        listy = []
        if len(s) >= 2:
            for i in range(len(s)):
                if len(listy) > 0 and s[i] == listy[-1]:
                    listy.pop(-1)
                    continue
                if s[i] in not_hasmapu:
                    return False
                listy.append(hashmapu[s[i]])
        else:
            return False
        return len(listy) == 0