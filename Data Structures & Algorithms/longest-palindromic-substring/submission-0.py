class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        '''

            Return the substring that is the longest palindrome
            Type of DP
                Max Value
            Define dp[i]
                potential middle ofpalindromic substring 
                at that index
                The max Palidromic sequnces tartgn from location
            Build Recurrence
                check if i+1 == i - 1
        '''

        # get the length of the input string
        n = len(s)

        # if the string is onl 1 or 2 then we just return len
        if n < 2:
            return s
        
        # create the 2d matrix, where each double index value
        # will represent the indices from two diff locations
        dp = [[False] * n for _ in range(n)]

        # varaibles to store largest palindrome so far
        # start refers to that starting index
        start = 0
        max_len = 1

        # set every position that is single len 1 to a palindrome
        for i in range(n):
            dp[i][i] = True
        
        # consider substring of len > 2
        # j is the right boundry of the sub string
        for j in range(1, n):
            # i is the left boundry
            for i in range(0, j):

                # sub string is palindrome if:
                    # characters on both end match

                    # inner substing is a palidrome

                        # either is only 2 chars

                        # of the inside var is also a palidrome

                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j]:
                    current_len = j - i + 1
                    if current_len > max_len:
                        max_len = current_len
                        start = i
        return s[start:start + max_len]









