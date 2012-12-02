import sys


def Move(RList,action):

    RoatateList = list(RList)
    len_list = len(RoatateList)
    quantity = RoatateList[action]
    RoatateList[action] = 0

    if quantity>0:
        i = action
        while quantity>0:
            if i+1>=len_list:
                i=0;
            else:
                i = i+1

            RoatateList[i] += 1
            quantity -= 1

        return RoatateList

    else:
        print 'The square doesnt have any squares'


def JustifyOver(RoatateList, input_n):
    len_list = len(RoatateList)
    half = len_list/2
    the_whole = input_n*input_n*2
    cal = 0
    for i in range(half):
        cal += RoatateList[i]

    if(cal == the_whole):
        print ';;;;;;A win;;;;;'
    elif(cal == 0):
        print ';;;;;;B win;;;;;'
    else:
        return False

    print 'finished already'
    return True


def printPebble(RoatateList):
    len_list = len(RoatateList)
    half = len_list/2
    list_A = list()
    list_B = list()
    list_A = RoatateList[:half]
    list_B = RoatateList[half:]
    list_B.reverse()
    print '--------- --------'
    print '[%s]' % ', '.join(map(str, list_A))
    print '[%s]' % ', '.join(map(str, list_B))



