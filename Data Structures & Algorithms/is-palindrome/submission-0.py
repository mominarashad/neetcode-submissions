class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [ch.lower() for ch in s if ch.isalnum()]

        low, high = 0, len(filtered) - 1
        while low < high:
            if filtered[low] != filtered[high]:
                return False
            low += 1
            high -= 1

        return True