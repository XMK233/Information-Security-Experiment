#coding=utf-8
from random import randint
import time

write = open('output.txt','w')
read = open('input.txt','r')

#模重复平方算法
def mochongfupingfang( b, n, m):
    c = '{0:b}'.format(n)
    a = 1
    n = []
    for i in range( 1 , len(c) + 1):
        n.append( int( c[-i] ) )
    for i in range( len(c) ):
        if n[ i ] == 1:
            a = a * b % m
            if i < len(c) - 1:
                b = b ** 2 % m
        else:
            a = a
            if i < len(c) - 1:
                b = b ** 2 % m
        
    return a

#判断最大公因数的函数
def gcd( a, b ):
    '''hui dai fa'''
    s = [ 0 ]
    t = [ 0 ]
    i = 0
    '''do some change if a is larger than b'''
    convertA = convertB = 1
    if a < 0 and b >= 0:
        a = abs( a )
        convertA = -1 
    elif b < 0 and a >= 0:
        b = abs( b ) 
        convertB = -1
    elif a < 0 and b < 0:
        a = abs( a )
        b = abs( b ) 
        convertA = -1 
        convertB = -1
    '''if the number is minus'''
    changePlace = 0
    if a > b:
        r0 = largerOne = a
        convertL = convertA
        r1 = smallerOne = b
        convertS = convertB
    else:
        r0 = largerOne = b
        convertL = convertB
        r1 = smallerOne = a
        convertS = convertA
        changePlace = 1
    '''the essence of the algorithm'''
    while True:
        '''if the 0 is one of the two number'''
        if a == 0 and b > 0:
            sFin = 0
            tFin = 1
            gcd = b 
            return gcd
            break
        elif b == 0 and a > 0:
            sFin = 1
            tFin = 0
            gcd = a 
            return gcd
            break 
        elif b == a == 0:
            sFin = 0
            tFin = 0
            gcd = 0
            return gcd
            break
        '''the other situation'''
        r2 = r0 % r1
        q = int( r0 / r1 )
        '''the smaller one is the gcd'''
        if r0 % r1 == 0 and i == 0:
            sFin = 0
            tFin = convertS 
            gcd = r1 
            if a > b:
                return gcd
            else:
                return gcd
            break    
        '''if the gcd need to do the  hui dai iteration'''   
        if r0 % r1 :
            if i == 0:
                s[ i ] = 1
                t[ i ] = -1 * q
            elif i == 1:
                s.append( -1 * q )
                t.append( -1 * q * t[ 0 ] + 1 )
            else:
                s.append( s[ i - 2 ] - q * s[ i - 1])
                t.append( t[ i - 2 ] - q * t[ i - 1])
            i += 1
            r0 = r1
            r1 = r2
        else:
            sFin = convertL * s[ len(s) - 1 ]
            tFin = convertS * t[ len(t) - 1 ]    
            gcd = r1
            if a > b:
                return gcd
            else:
                return gcd
            break
        '''get the time'''

#循环次数
k = 10

#核心部分
for j in range(10):
    n = int( read.readline() )
    strTime = time.time()
    #如果录入的数字是1或者0
    if n == 1 or n == 0:
        print( "not" )
        endTime = time.time()
        write.write('not. the time is:' + str(endTime - strTime) + '\n')
    #因为如果是小于10的数就会出错，所以将10以内的素数全部列举出
    elif n == 2 or n == 3 or n == 5 or n == 7:
        print("yes")
        endTime = time.time()
        write.write('yes. the time is:' + str(endTime - strTime) + '\n')
    #如果是大数
    else:
        for i in range ( k ):#在循环次数之内
            b = randint(2, n - 1)#随机得到b
            d = gcd( b , n )#得到最大公因数
            if d > 1:#如果还有公因数就不是质数
                print( "not" )
                endTime = time.time()
                write.write('not. the time is:' + str(endTime - strTime) + '\n')
                break
            else:
                c = mochongfupingfang(b, (n - 1), n)#互质的话就测试b^(n-1)是否与1同余
                if c != 1:#不同余，不是质数
                    print( "not" )
                    endTime = time.time()
                    write.write('not. the time is:' + str(endTime - strTime) + '\n')
                    break
                if i == k - 1:#是伪质数
                    print("yes")
                    endTime = time.time()
                    write.write('yes. the time is:' + str(endTime - strTime) + '\n')
                else:#在检测一轮
                    continue
read.close()
write.close()