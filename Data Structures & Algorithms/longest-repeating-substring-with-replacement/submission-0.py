class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # freq map for the window
        count = defaultdict(int)

        # left pointer
        left = 0

        # max frequency or single character in window
        max_count = 0
        res = 0

        # iterate through potential window sizes by changing right pointer
        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])

            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right-left + 1)

        return res
