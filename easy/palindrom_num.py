class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = list(str(x))
        palindrom = list(reversed(original))
        
        return original == palindrom