class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = "".join(char.lower() for char in s if char.isalnum())
        return alphanum[::-1] == alphanum