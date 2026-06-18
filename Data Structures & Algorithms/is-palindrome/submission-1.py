class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = "".join(char for char in s if char.isalnum())
        return alphanum.lower()[::-1] == alphanum.lower()