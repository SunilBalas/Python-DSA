from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

s = Solution()
print(s.isAnagram("anagram", "nagaram"))