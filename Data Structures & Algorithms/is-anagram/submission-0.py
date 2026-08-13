class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        hashMap2 = {}

        for letters in s:
            if letters in hashMap:
                hashMap[letters] += 1
            else:
                hashMap[letters] = 1

        for letters2 in t:
            if letters2 in hashMap2:
                hashMap2[letters2] += 1
            else:
                hashMap2[letters2] = 1

        return hashMap == hashMap2