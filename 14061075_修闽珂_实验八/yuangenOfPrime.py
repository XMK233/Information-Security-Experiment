#coding=utf-8
import math 
import random
from random import randint
import time
#最大公因数
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
#素性检验
def millerRabin( n ):
    t = 10
    previous = [2, 3, 5, 7, 11, 13, 17]
    if previous.count(n) != 0:
        return True
    if n % 2 == 0:
        return False
    else:
        r = n - 1
        s = 0
        while r % 2 == 0: 
                r = r // 2
                s = s + 1 
        for i in range(t):
            a = randint(0, n - 2)
            y = mochongfupingfang(a, r, n)
            if y != 1 and y != n - 1:
                j = 1
                while (j <= s - 1 and y != n - 1):
                    y = mochongfupingfang(y, 2, n) 
                    if y == 1 :
                        return False
                    j = j + 1
                if y != n - 1:
                    return False
            else:
                return True

#质因数的算法
def getfactor(num):
    l = []
    if millerRabin(num):
        return [num]
    for n in range(2, num + 1):
        if num % n == 0 and millerRabin(n):
            if l.count(n) == 0: 
                l.append(n)
    return l
#原根的判断法
def isYuangen(a, x):
    x = int(x)
    p = getfactor(x - 1)
    for i in range(len(p)):
        if mochongfupingfang(a, (x-1) // p[i], x) == 1:
            return False
    return True
#欧拉函数
def Euler(n):
    n = int(n)
    count = 0
    for i in range(1,n):
        if gcd(i, n) == 1:
            count = count + 1
    return count
#生成随机质数
f = open('output.txt', 'w')
time1 = time.time()
while True:
    t = randint(2 ** 15, 2 ** 16 - 1)
    if millerRabin(t):
        break
#t = input("the target: ")
#print(t)
f.write(str(t))
f.write('\n')
f.write("原根：")
f.write('\n')
#
k = 0
a = 2
while k < 10:
    if isYuangen(a, t):
        #print(a)
        f.write(str(a))
        f.write('\n')
        if k == 0:
            min = a
        k = k + 1
    a = a + 1 
    if a == t:
        break
#
num = Euler(Euler(t))
#print(num)
f.write("原根的数量是：")
f.write(str(num))
f.write('\n')
#
t = int(t)
f.write("离散对数表：")
f.write('\n')
for i in range(t):
    if i == t - 2:
        break
    #print(i + 1, " ", mochongfupingfang(min, i + 1, t))
    f.write(str(i + 1))
    f.write(" ")
    f.write(str(mochongfupingfang(min, i + 1, t)))
    f.write('\n')
time2 = time.time()
f.write("时间是：")
f.write(str(time2 - time1))
f.close()

    
    
