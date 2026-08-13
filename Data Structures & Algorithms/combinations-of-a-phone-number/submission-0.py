class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        '''

        Create some sort of map to hold the number to letters

        '''

        if not digits:
            return []
        
        # Map from digit to possible letters
        phone_map = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []

        def backtrack(index, path):

            if index == len(digits):
                result.append(path)
                return

            potential_chars = phone_map[digits[index]]

            for char in potential_chars:
                backtrack(index + 1, path + char)

        backtrack(0, "")
        return result

            
            







