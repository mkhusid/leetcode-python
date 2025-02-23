class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] != '(' and s[0] != '[' and s[0] != '{':
            return False

        counter_r, counter_s, counter_f = 0, 0, 0

        expected_closes = []

        for p in s:
            if (p == ']' or p == ')' or p == '}')\
                and (len(expected_closes) == 0 or p != expected_closes.pop()):
                return False

            if p == '(':
                counter_r += 1
                expected_closes.append(')')
            elif p == ')':
                counter_r -= 1

            if p == '[':
                counter_s += 1
                expected_closes.append(']')
            elif p ==  ']':
                counter_s -= 1

            if p == '{':
                counter_f += 1
                expected_closes.append('}')
            elif p ==  '}':
                counter_f -= 1

        return counter_r == 0 and counter_s == 0 and counter_f == 0