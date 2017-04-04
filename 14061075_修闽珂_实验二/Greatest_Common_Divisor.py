'''hui dai fa'''
import time

a = int( input ( "the a is: " ) )
b = int( input ( "the b is: " ) )
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
strTime = time.time()
while True:
    '''if the 0 is one of the two number'''
    if a == 0 and b > 0:
        sFin = 0
        tFin = 1
        gcd = b 
        print ( "the s, t and gcd( a,b ) is: ", sFin , tFin , gcd)
        break
    elif b == 0 and a > 0:
        sFin = 1
        tFin = 0
        gcd = a 
        print ( "the s, t and gcd( a,b ) is: ", sFin , tFin , gcd)
        break 
    elif b == a == 0:
        sFin = 0
        tFin = 0
        gcd = 0
        print ( "the s, t and gcd( a,b ) is: ", sFin , tFin , gcd)
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
            print ( "the s, t and gcd( a,b ) is: ", sFin ,",",  tFin ,",",  gcd)
        else:
            print ( "the s, t and gcd( a,b ) is: ", tFin , sFin , gcd)
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
            print ( "the s, t and gcd( a,b ) is: ", sFin , tFin , gcd)
        else:
            print ( "the s, t and gcd( a,b ) is: ", tFin , sFin , gcd)
        break
    '''get the time'''
   
endTime = time.time()        
print ( "the time is: ", endTime - strTime, "s")
        
    