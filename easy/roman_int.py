class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        symbols = list(s)
        
        for i, curr in enumerate(symbols):
            try:
                nxt = symbols[i+1]
                if romans[curr] >= romans[nxt]:
                    result += romans[curr]
                else:
                    result -= romans[curr]
            except KeyError:
                print(f"Wrong character!")
                break   
            except IndexError:
                result += romans[curr]
                print('End of string.')
                    
        return result 