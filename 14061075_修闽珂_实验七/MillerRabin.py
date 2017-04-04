#中文你支持不支持？
import math 
import random
from random import randint
#
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
#
def millerRabin( n ):
    t = 10
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
                    
def main():
    f = open ( 'output.txt' , 'w')
    number = 0
    while number <2:
        n = randint(3, 100)
        if millerRabin(n):
            f.write ( str(n) )
            f.write( '\n')
            print(int(n))
            number = number + 1
    number = 0
    while number < 10:
        n = randint(2 ** 127, 2 ** 128-1)
        if millerRabin(n):
            f.write ( str(n) )
            f.write( '\n')
            print(int(n))
            number = number + 1
    f.close()
    '''101, 1000'''
if __name__ == '__main__':
    main()


    
    
    
