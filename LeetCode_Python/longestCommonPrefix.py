class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        kkkkkk
        """

        self.strList = []
        self.contador = 0
        self.rtype = ""
        

        
        if len(strs) > 1:
            for letra in range(len(strs[0])):    
                for palavra in range(len(strs)):
                    if(palavra < len(strs) - 1 and letra < len(strs[palavra + 1])):
                        if len(strs[palavra]) > letra and strs[palavra][letra] == strs[palavra + 1][letra]:
                            self.contador += 1

                if self.contador == (len(strs) - 1):
                    self.strList.append(strs[0][letra])
                    self.contador = 0
                else:
                    break
        
                        
            self.rtype = "".join(self.strList)
            
        elif (strs != None and strs != ([]) and strs[0] != self.rtype):
            self.rtype = strs[0][0]

        return self.rtype
        

#test = Solution()
#print(test.longestCommonPrefix(["flowe","flowrrr","flowrrrrr"]))