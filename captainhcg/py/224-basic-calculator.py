class Solution(object):
    def calculate(self, s):
        s = "".join([c for c in s if c != " "])
        s = "(" + s + ")"
        s = s.replace("(-", "(0-")

        num_stack = []
        op_stack = []
        
        def cal():
            while op_stack and op_stack[-1] in ("+-"):
                n2, n1, op = num_stack.pop(), num_stack.pop(), op_stack.pop()
                if op == "+":
                    num_stack.append(n1 + n2)
                else:
                    num_stack.append(n1 - n2)
        
        last_number = ""
        for ch in s:
            if ch.isdigit():
                last_number = last_number + ch
            else:
                if last_number:
                    num_stack.append(int(last_number))
                    last_number = ""
                    cal()
                if ch in "(+-":
                    op_stack.append(ch)
                else:
                    op_stack.pop()
                    cal()
        
        return num_stack.pop()
