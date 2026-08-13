class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        unique_chars = set()
        max_size = 0

        for r in range(len(s)):
        
            while s[r] in unique_chars:
                unique_chars.remove(s[l])
                l += 1
            
            unique_chars.add(s[r])

            max_size = max(max_size, len(unique_chars))


        return max_size

