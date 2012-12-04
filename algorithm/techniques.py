#!/usr/bin/python
from __future__ import division
import pdb
import sys
from hashDict import dict_hash
from utils import Move

class Alpha_Beta:

    PositiveExtreme = sys.maxint
    NegativeExtreme = -sys.maxint-1
    RotateList =[]


    def __init__(self, input_n, d):
        self.input_n = input_n
        self.d = d
        self.let_who_win= 'A'
        self.RotateList =[]
#        self.logger = logging.getLogger()
#        handler=logging.FileHandler("Log_game.txt")
#        self.logger.addHandler(handler)
#        self.logger.setLevel(logging.NOTSET)
#        self.logger.error("start logging")

        for x in range(input_n*2):
            self.RotateList.append(input_n)
            self.len_list = input_n*2


    def Search(self, Clever_Stupid, label):
        dictHash = dict_hash(self.input_n, label, Clever_Stupid)
        self.let_who_win= label
        dict_ret = self.MAX_Value(self.RotateList, self.NegativeExtreme, self.PositiveExtreme, dictHash, label,1)
        del dictHash
        if dict_ret['label1']:
            return dict_ret['label3']


    def MAX_Value(self, RList, alpha, beta, dictHash, label, depth):

        if dictHash.checkDuplicate(RList, label):
            return {'label1':False}

        dictHash.append(RList, label)

        half = self.len_list//2
        label_start = 0
        if label== 'A':
            label_start = 0
        else:
            label_start = 1
        start = label_start*half
        if self.Terminal_test(RList,depth):
            winOrLose = dictHash.Utility(RList, self.let_who_win)
            return {'label1':True, 'label2':winOrLose}

        v = self.NegativeExtreme
        dict_ret = {}
        RListAction = list()
        index = -1
        for i in range(half):
            if RList[start+i]>0:
                RlistAction = Move(RList,start+i)

   #             dictHash.printDictHash()
    #            print '-----MAX_VALUE-----'
     #           print RList,RListAction

                dict_ret = self.MIN_Value(RlistAction, alpha, beta, dictHash, chr(66-label_start), depth)
                if(dict_ret['label1']==False):
#                    self.logger.debug('fail in MAX_value duplicate')
                    continue

                if max(v,dict_ret['label2']) > v:
                    v = dict_ret['label2']
                    index = start+i
#                    self.logger.debug("Trying to get a MAX_Value v:%d, index:%d, a:%d, b:%d", v, index, alpha, beta)

                if v>=beta:
                    return {'label1':True, 'label2':v, 'label3':index}
                alpha = max(alpha,v)

        return {'label1':True, 'label2':v, 'label3':index}


    def MIN_Value(self, RList, alpha, beta, dictHash, label, depth):
#        print 'Rlist = ', RList, label
        if dictHash.checkDuplicate(RList, label):
            return {'label1':False}

        dictHash.append(RList, label)

        half = self.len_list//2
        label_start = 0
        if label== 'A':
            label_start = 0
        else:
            label_start = 1
        start = label_start*half

        if self.Terminal_test(RList, depth):
            winOrLose = dictHash.Utility(RList, self.let_who_win)
            return {'label1':True, 'label2':winOrLose}
        v = self.PositiveExtreme
        dict_ret = {}
        index = -1
        RListAction = list(RList)
        for i in range(half):
            if RList[start+i]>0:
                RListAction = Move(RList,start+i)
  #              dictHash.printDictHash()
   #             print '----MIN_VALUE------'
        #        print RList,RListAction

                dict_ret = self.MAX_Value(RListAction, alpha, beta, dictHash, chr(66-label_start), depth+1)
                if(dict_ret['label1']==False):
                    continue


                if min(v,dict_ret['label2']) < v:
                    v = dict_ret['label2']
                    index = start+i
#                    self.logger.debug("Trying to get a MIN_Value v:%d, index:%d, a:%d, b:%d", v, index, alpha, beta)

                if v<=alpha:
                    return {'label1':True, 'label2':v, 'label3':index}
                beta = min(beta,v)

        return {'label1':True, 'label2':v, 'label3':index}

    def Terminal_test(self, RList, depth):

        cal = 0
        for i in range(self.input_n):
            cal += RList[i]

        the_whole = self.input_n*self.input_n*2
        if(cal==the_whole or cal==0 or depth>=self.d):
            return True
        return False


    def change(self, action):
        RoatateList = self.RotateList
        len_list = len(RoatateList)
        quantity = RoatateList[action]
        RoatateList[action] = 0
        if quantity>0:
            i = action
            while quantity>0:
                if i+1>=len_list:
                    i=0
                else:
                    i = i+1
                RoatateList[i] += 1
                quantity -= 1
            return True
        else:
            print 'The square you input doesnt have any squares'
            return False


    def re_construct_pebble(self, *kargs):
        def constructFromTwo(self,A,B):
            B.reverse()
            self.RotateList = A+B
        def constructFromOne(self, whole_list):
            self.RotateList = whole_list
        if len(kargs)==2:
            return constructFromTwo(self, *kargs)
        else:
            return constructFromOne(self, *kargs)

