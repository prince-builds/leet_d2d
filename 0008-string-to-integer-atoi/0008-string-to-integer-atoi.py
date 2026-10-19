class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        
        # 1. Discard leading whitespace
        while i < n and s[i] == ' ':
            i += 1
            
        if i == n:
            return 0
        
        # 2. Determine sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # 3. Read digits and clamp to 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        total = 0
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Check overflow/underflow before adding the next digit
            if total > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            total = total * 10 + digit
            i += 1
            
        return sign * total