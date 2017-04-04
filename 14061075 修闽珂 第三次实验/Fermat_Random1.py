#coding=utf-8 
import random
from random import randint
f = open('input.txt','w')    

numSmall = random.randint(1,9)
numBig = 10 - numSmall

numOfSmall = numOfBig = 1
for i in range (0,10):
    k = random.randint( 0,1 )
    if k == 0 and numOfSmall <= numSmall:#随机的位置生成大或小数
        print(random.randint(0,100))
        f.write ( str(random.randint(0,100)) )
        f.write( '\n')
    else:
        p = 1
        digit = random.randint(3,10000)
    #产生大数的位数
    
        for j in range ( digit ):
        #在位数内循环ֵ
            if p == 1:
            #如果是第一位，不能为零，不换行
                print(randint(1,9), end = '')
                f.write ( str(randint(1,9)) )
                p += 1
            elif j < (digit - 1):#第二位开始任意赋值，不换行
                print(randint(0,9), end = '')
                f.write ( str(randint(0,9)) )
            else:
            #最后一个数，换行
                print(randint(0,9))
                f.write ( str(randint(0,9)) )
                f.write ( '\n' )
                break        

f.close()