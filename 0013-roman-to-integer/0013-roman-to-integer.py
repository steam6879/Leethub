class Solution:
    def romanToInt(self, s: str) -> int:
        roman_table = {'I': 1,
                       'V': 5,
                       'X': 10,
                       'L': 50,
                       'C': 100,
                       'D': 500,
                       'M': 1000}
        n = len(s)
        s_list = list(s)
        out = 0
        ptr = 0
        if n == 1:
            out = roman_table[s_list[0]]
            return out
        while ptr < n - 1:
            if roman_table[s_list[ptr]] > roman_table[s_list[ptr + 1]]:
                out += roman_table[s_list[ptr]]

                if ptr == n - 2:
                    out += roman_table[s_list[ptr + 1]]
                    ptr += 1
                    break
                ptr += 1
            
            elif roman_table[s_list[ptr]] == roman_table[s_list[ptr + 1]]:
                out += roman_table[s_list[ptr]]

                if ptr == n - 2:
                    out += roman_table[s_list[ptr + 1]]
                    
                ptr += 1
                
            else:
                out += roman_table[s_list[ptr + 1]] - roman_table[s_list[ptr]]
                ptr += 2
                if ptr == n - 1:
                    out += roman_table[s_list[ptr]]
        
        return out
