
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need_freq = defaultdict(int)
        have_freq = defaultdict(int)

        for char in t:
            need_freq[char] += 1

        have = 0
        need = len(need_freq)

        left = 0
        best_length = float("inf")
        best_start = 0

        for right in range(len(s)):
            char = s[right]
            have_freq[char] += 1

            # This character's required frequency is now satisfied.
            if char in need_freq and have_freq[char] == need_freq[char]:
                have += 1

            # Shrink the window while it remains valid.
            while have == need:
                window_length = right - left + 1

                if window_length < best_length:
                    best_length = window_length
                    best_start = left

                left_char = s[left]
                have_freq[left_char] -= 1

                # Removing this character made the window invalid.
                if (
                    left_char in need_freq
                    and have_freq[left_char] < need_freq[left_char]
                ):
                    have -= 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_start : best_start + best_length]


