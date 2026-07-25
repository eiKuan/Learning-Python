class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if ( (len(s) % 2) != 0):
            self.rtype = False
        else:
            self.open = ["{", "[", "("]
            self.close = ["}", "]", ")"]
            self.deuBosta = False
            self.charList = list(s)
            
            while(len(self.charList) > 1 and self.deuBosta == False):
                
                    self.ultimoAberto = "x"
                    
                    for i in range(len(self.charList)):
                        if self.charList[i] in self.open:
                            self.ultimoAberto = i
                            self.parenAtual = self.open.index(self.charList[i])
                            
                    if self.ultimoAberto == "x":
                        break
                    
                    for i in range(len(self.charList)):
                        if ((len(self.charList) - 1 - i) <= self.ultimoAberto):
                            self.deuBosta = True
                            break
                        
                        elif( (self.ultimoAberto + 1 + i) < len(self.charList) ):
                            if self.close[self.parenAtual] == self.charList[self.ultimoAberto + 1 + i]:
                                self.charList.pop(self.ultimoAberto + 1 + i)
                                self.charList.pop(self.ultimoAberto)
                                break
                            else:
                                self.deuBosta = True
                                break
                        else:
                            self.deuBosta = True
                            break
                        
            if len(self.charList) == 0:
                self.rtype = True
            else:
                self.rtype = False


        return self.rtype
    
#test = Solution()
#print(test.isValid("]}]"))