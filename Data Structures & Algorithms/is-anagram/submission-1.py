class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashSetS, hashSetT = {}, {}

        for i in range(len(s)):
            hashSetS[s[i]] = 1 + hashSetS.get(s[i], 0)
            hashSetT[t[i]] = 1 + hashSetT.get(t[i], 0)
        return hashSetS == hashSetT