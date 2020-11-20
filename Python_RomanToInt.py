class Solution:
    def romanToInt(self, s: str) -> int:
        num  = 0
        i = 0
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        while i < len(s)-1:
            if dic[s[i]] >= dic[s[i+1]]:
                num = num + dic[s[i]]
                i = i + 1
                flag = True
            else:
                num = num + dic[s[i+1]] - dic[s[i]]
                i = i + 2
                flag = False
        
        if flag:
            num = num + dic[s[-1]]

        return num 

val = Solution()
print(val.romanToInt("MCMXCIV"))