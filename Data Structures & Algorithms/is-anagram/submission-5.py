class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        list_s = [0] * 26
        list_t = [0] * 26

        for i in range(len(s)):
            loc_s = ord(s[i]) - ord('a')
            loc_t = ord(t[i]) - ord('a')
            list_s[loc_s] += 1
            list_t[loc_t] += 1

        if list_s == list_t:
            return True
        return False



