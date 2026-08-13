class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for i in range(len(s)):
            loc_s = ord(s[i]) - ord('a')
            loc_t = ord(t[i]) - ord('a')
            count[loc_s] += 1
            count[loc_t] -= 1

        print(count)

        for s in count:
            if s != 0:
                return False
        return True



