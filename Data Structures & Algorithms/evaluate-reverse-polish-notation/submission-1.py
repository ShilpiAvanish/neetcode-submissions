class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # use a stack to push the numebrs in the stack 

        # use another stack to push the art in
        arth_set = ["+", "-", "*", "/"]
        arth = set(arth_set)
        num_stack = []

        for token in tokens:

            if token in arth_set:

                second_num = int(num_stack.pop())
                first_num = int(num_stack.pop())
                new_num = 0

                if token == "+":
                    new_num = first_num + second_num
                if token == "-":
                    new_num = first_num - second_num
                if token == "*":
                    new_num = first_num * second_num
                if token == "/":
                    new_num = int(first_num / second_num)

                num_stack.append(new_num)
            else:
                num_stack.append(int(token))
        
        return num_stack[0]
            

