"""
    Collection of collaborative filtering techniques:
"""
from __future__ import division
class dict_hash:

    def __init__(self, input_n, label, Clever_Stupid):
        self.nValue = input_n
        self.the_whole = self.nValue*self.nValue*2
        self.Bidict=dict()
        self.Bidict={'A':{}, 'B':{}}
        if Clever_Stupid == 'stupid':
            self.Utility = self.Utility_stupid
        else:
            self.Utility = self.Utility_intelligent


    def checkDuplicate(self, Rlist, label):
        Dict = self.Bidict[label]
        Index = 0
        for x in range(self.nValue):
            Index += Rlist[2*x]*Rlist[2*x+1]
            Index += Rlist[2*x]

        if Dict.has_key(Index):
            value = Dict[Index]
            for k in value:
                x = 0
                for x in range(self.nValue*2):
                    if not k[x] == Rlist[x]:
                        break
                if x == self.nValue*2 -1:
                    return True

            return False;
        else:
            self.Bidict[label][Index] = []
            return False;

    def append(self, Rlist, label):

        Index = 0
        for x in range(self.nValue):
            Index += Rlist[2*x]*Rlist[2*x+1]
            Index += Rlist[2*x]

        newList = list(Rlist)
        self.Bidict[label][Index].append(newList)

    def delete(self, Rlist, label):

        Index = 0
        for x in range(self.nValue):
            Index += Rlist[2*x]*Rlist[2*x+1]
            Index += Rlist[2*x]
        self.Bidict[label][Index].remove(Rlist)

    def IntelligentUtility(self, RList, self_list):
        cal = 0

        if(self.nValue<=4):
            half = self.nValue//2
            for i in range(half-1):
                cal += RList[i]
            
            for i in range(self.nValue):
                cal += RList[i]*(self.nValue-i)/self.nValue
            ret_result = (self.the_whole-cal)/self.the_whole

            if ret_result<0:
                return 0
            else:
                return ret_result
            
        else:
            for i in range(self.nValue):
                cal += self_list[i]*(self.nValue-i)/self.nValue
     
            for i in range(self.nValue):
                cal += RList[i]*(i+1)/self.nValue
            
            ret_result = cal/self.the_whole
            return ret_result


    def Utility_intelligent(self, RList, let_who_win):
        cal = 0
        for i in range(self.nValue):
            cal += RList[i]
        if(cal==0):
            if(let_who_win=='A'):
                return 0
            else:
                return 1
        elif cal==self.the_whole:
            if(let_who_win=='A'):
                return 1
            else:
                return 0
        else:
            if(let_who_win=='A'):
                List_B= RList[self.nValue:]
                self_list = list()
                self_list = RList[:self.nValue]
                return self.IntelligentUtility(List_B, self_list)
            else:
                List_A= RList[:self.nValue]
                self_list = list()
                self_list = RList[self.nValue:]
                return self.IntelligentUtility(List_A, self_list)


    def Utility_stupid(self, RList, let_who_win):
        cal = 0
        for i in range(self.nValue):
            cal += RList[i]
        if(cal==0):
            if(let_who_win=='A'):
                return 0
            else:
                return 1
        elif cal==self.the_whole:
            if(let_who_win=='A'):
                return 1
            else:
                return 0
        else:
            if(let_who_win=='A'):
                return cal/self.the_whole
            else:
                return 1-cal/self.the_whole


    def printDictHash(self):
        print self.Bidict
