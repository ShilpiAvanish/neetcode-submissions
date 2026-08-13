class Solution:
    def countSubstrings(self, s: str) -> int:
        
        '''

        Intuition:
            expand out from center if a valid palindrome

            two options
            -> even palindrome
            -> odd palindrome

            iterate over the string
                first check if odd

                secon check for even palindrome
        '''
        total = 0
        l, r = 0, 0
        for i, c in enumerate(s):
            
            l = r = i
            while (l > -1 and r < len(s)):
                
                if s[l] == s[r]:
                    total += 1
                    l-=1
                    r+=1
                else: break


            l , r = i, i + 1
            while (l > -1 and r < len(s)):
                
                if s[l] == s[r]:
                    total += 1
                    l-=1
                    r+=1
                else: break

        return total