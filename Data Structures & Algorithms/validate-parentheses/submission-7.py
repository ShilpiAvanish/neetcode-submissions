class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        close_open = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        for char in s:

            if char in "([{":
                stack.append(char)


            elif stack and char in close_open:

                if stack[-1] == close_open[char]:
                    stack.pop()

                else:
                    return False

            else:
                return False

        return not stack


