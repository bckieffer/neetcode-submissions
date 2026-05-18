class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        diff = list(set(s) - set(t))

        if(diff):
            return False

        if sorted(s) != sorted(t):
            return False

        return True
        