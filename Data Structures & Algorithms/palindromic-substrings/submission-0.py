class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)

        count = 0

        def expand(left, right):

            pal_count = 0
            while left>=0 and right<n and s[left] == s[right]:
                pal_count += 1
                left -= 1
                right += 1
            return pal_count




        for i in range(n):

            count += expand(i, i)
            count += expand(i, i + 1)

        return count