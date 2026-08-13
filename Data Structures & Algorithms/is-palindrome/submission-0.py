class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string = []
        
        for letter in s:
            if letter.isalnum():
                string.append(letter.lower()) 
        
        for index in range(len(string) // 2):
            if string[index] != string[len(string) - index - 1]:
                return False
        
        return True
