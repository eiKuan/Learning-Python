class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x < 0):
            self.rtype = False
        else:

            self.tamanho = 0
            self.qtd = 0

            while(x // (10 ** self.tamanho) != 0):
                self.tamanho += 1

            self.metade = self.tamanho // 2

            
            for i in range(self.tamanho):
                casaUm = (x % 10 ** (self.tamanho - i) ) // 10 ** (self.tamanho - (i + 1) )
                casaOposta= (x % 10 ** (i + 1) ) // 10 ** i

                if(casaUm == casaOposta) and i < self.metade:
                    self.qtd += 1

            if(self.qtd == self.metade):
                self.rtype = True
            else:
                self.rtype = False

        return self.rtype

#test = Solution()
#print(test.isPalindrome(121))