class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        self.romano = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        s = s.upper()
        self.rtype = 0
        self.i = 0
       
       #Nao sei nem como isso aqui funcionou nos tres primeiros cases
        while self.i < (len(s)):
            if( self.i < len(s) - 1 ):
                if (self.romano[s[self.i + 1]] > self.romano[s[self.i]]):
                    result = self.romano[s[self.i + 1]] - self.romano[s[self.i]]
                    self.rtype += result 
                    self.i += 1
                else:
                    self.rtype += self.romano[s[self.i]]
            elif(self.i == len(s) - 1):
                self.rtype += self.romano[s[self.i]]

            self.i += 1
        
        return self.rtype

#test = Solution()
#print(test.romanToInt("MCMXCIV"))