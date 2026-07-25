
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        self.l1Aux = list1
        self.rtype = self.l1Aux
        self.l2Aux = list2


        if (self.l1Aux  == None):
            self.rtype = self.l2Aux
        else:
            while(self.l2Aux != None):
                if(self.l2Aux.val >= self.l1Aux.val):

                    if (self.l1Aux.next != None):

                        if(self.l2Aux.val <= self.l1Aux.next.val):
                            AuxAux = ListNode(self.l2Aux.val, self.l1Aux.next)
 

                            self.l1Aux.next = AuxAux
                        else:
                            self.l1Aux = self.l1Aux.next
                            continue
                    else:
                        self.l1Aux.next = self.l2Aux
                        break
                else:
                    AuxAux = ListNode(self.l2Aux.val, self.l1Aux)
                    self.l1Aux = AuxAux
                    self.rtype = self.l1Aux


                self.l2Aux = self.l2Aux.next    
                
        return self.rtype
    
            
  
# test = Solution()

# list1 = (ListNode(2,ListNode(2,ListNode(4))))

# list2 = (ListNode(1,ListNode(3,ListNode(4))))

# result = test.mergeTwoLists(list1, list2)
# print("PRINT..................")
# while result != None:
#     print(result.val)
#     result = result.next