class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # handle this edge case if s or t does not exist
        if not s or not t:
            return ""
        
        # count the frequency of characters in t
        t_count = Counter(t)
        required = len(t_count)

        l, r = 0, 0

        window_count = defaultdict(int)

        # How many chars in t ares satisfied in the window
        formed = 0

        ans = float("inf"), None, None

        while r < len(s):
            char = s[r]

            # add char to the window
            window_count[char] += 1

            # check if char's count matches t's requirements
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            while l <= r and formed == required:
                char = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
                
                l += 1
            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
