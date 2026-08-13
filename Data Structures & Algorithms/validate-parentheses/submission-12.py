class Solution:
    def isValid(self, s: str) -> bool:


        # hold a stack 

        close_bracket = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }

        bracket_stack = []

        for brack in s:
            if brack in close_bracket.keys():
                if not bracket_stack:
                    return False
                if bracket_stack.pop() != close_bracket[brack]:
                    return False

            else:
                bracket_stack.append(brack)
        if len(bracket_stack) == 0:
            return True
        return False

    