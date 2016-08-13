class Solution(object):
    def calculate(self, s):
        from operator import truediv
        def get_eles(s):
        	last_n = ""
        	for ch in s.replace(" ", ""):
        		if ch in "+-*/":
        			yield last_n
        			yield ch
        			last_n = ""
        		else:
        			last_n += ch
        	yield last_n
        	
        numbers = []
        op = "+"
        for n in get_eles(s):
            if not n.isdigit():
                op = n
            else:
                n = int(n)
                if op == "+":
                    numbers.append(n)
                elif op == "-":
                    numbers.append(-n)                
                elif op == "*":
                    numbers.append(numbers.pop() * n)
                else:
                    numbers.append(int(truediv(numbers.pop(), n)))
                    
        return sum(numbers)
