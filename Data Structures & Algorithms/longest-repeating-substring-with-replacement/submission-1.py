class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        letter_freq = defaultdict(int)
        res = 0

        for r in range(len(s)):

            letter_freq[s[r]] += 1

            while (r - l + 1) - max(letter_freq.values()) > k:
                letter_freq[s[l]] -= 1
                l += 1


            res = max(res, r-l+1)

        return res