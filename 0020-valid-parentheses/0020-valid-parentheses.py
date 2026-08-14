class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pairs = { ')':'(', ']':'[', '}':'{'}

        for ch in s:
            if ch in "([{":
                stk.append(ch)
            elif stk and stk[-1]==pairs[ch]:
                stk.pop()
            else:
                return False
        return len(stk) == 0