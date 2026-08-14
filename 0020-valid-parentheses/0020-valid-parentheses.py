class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for i in s:
            if i=='(' or i == '[' or i == '{':
                stk.append(i)
            elif len(stk)!= 0 and i == ')' and stk[-1] == '(':
                stk.pop()
            elif len(stk)!= 0 and i == ']' and stk[-1] == '[':
                stk.pop()
            elif len(stk)!= 0 and i == '}' and stk[-1] == '{':
                stk.pop()
            else:
                return False
        if len(stk) == 0:
            return True
        return False