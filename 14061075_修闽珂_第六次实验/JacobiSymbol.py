#coding=utf-8
'''def jacobiSymbol(v, up, down):
    if (up % down) == 0:#； 
        return
    if (up > down):#
        up = up % down
    if up % 2 == 0:
        v = v * -1 ** ((down**2 - 1)/8)
        up = up / 2
        jacobiSymbol(v, up, down)
    v = ((-1) ** ((up - 1)/2) )** ((down - 1)/2)
    jacobiSymbol(v, down, up)
 '''  
from random import randint

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
       
def mochongfupingfang( b, n, m):#模重复平方算法
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
#所有的除都是整除，不是普通除法，这个要结合python的特点来使用
def jacobiSymbol1(up, down): #雅可比符号：运用二次互反率
    v = 1
    while True:
        if up < 0:#判断上面的数字up是不是大于零，是则继续，否则上面的数加上下面的数字down为上面的数字。
            up = up + down
            continue
        if up % 2 == 0:#b)    判断上面的数字是不是偶数，如果是，就分出来一个（2/down）（(up/2)/down），左边的符号可以用公式来计算，后面的部分返回a)进行判断.
            v = v * ((-1) ** ((down**2 - 1)//8))
            up = up // 2
            continue
        if up % down == 0 :#c)    判断上面的是否能整除下面的。如果能且此时下面的数字是一则返回零，结束。否则返回v，结束
            if down != 1:
                return 0 
            break
        if (up > down):#d)    判断上面的是否大于下面的数字，是则上面的数字为up % down。判断上面的数字是不是2，如果是就可以返回最终值v并结束函数了。否则返回a)
            up = up % down
            #
            if up == 2:#e)    若以上判断皆为否，则进行一下操作：v = v * (((-1) ** ((up - 1)/2) )** ((down - 1)/2))（注：**为乘方），接着上下互反,返回a).
                v = v * ((-1) ** ((down**2 - 1)//8))
                return v
            #
            continue
        v = v * (((-1) ** ((up - 1)//2) )** ((down - 1)//2))
        temp = up
        up = down
        down = temp
    return v
    
def main():
    #jvalue = 1
    fileIn = open("input.txt", "r")
    fileOut = open("output.txt","w") 
    '''up = int(input())
    down = int( input())'''
    for i in range(10):
        if i < 5:
            k = fileIn.readline()
            a, b = k.split()
            up = int(a)
            down = int(b)
            if up % down == 0:
                fileOut.write(str(0) + '\n')
                print("0")
            else:
                jvalue = jacobiSymbol1(up, down)
                fileOut.write(str( int(jvalue) ) + '\n')
                print( str( int(jvalue) ) )
        else:#这就是SS算法，照本宣科而已
            a = fileIn.readline()
            n = int( a )
            for k in range(10):
                b = randint(2, n-2)
                d = gcd(b, n)
                if d > 1:
                    fileOut.write("no" + '\n')
                    print("no")
                    break
                r = mochongfupingfang(b, (n - 1)//2, n)
                if r != 1: 
                    r = r - n
                if r == 1 or r ==  -1:
                    pass
                else:
                    fileOut.write("no" + '\n')
                    print("no")
                    break        
                    '''if (r - n) != -1:
                        '''
                s = jacobiSymbol1(b, n)
                if r != s :
                    fileOut.write("no" + '\n')
                    print("no")
                    break
                else:
                    if k == 9:
                        fileOut.write("yes" + '\n')
                        print("yes")
                        break
                    continue
            
            
    fileIn.close()
    fileOut.close()

if __name__ == '__main__':
    main() 
        