import time

upLimit = int(input ("input range: "))

#将所有的数组元素统统设置成1，第一个数设为零，意为1不是质数
startTime = time.time()
whleList = [1] * upLimit
whleList[ 0 ] = 0

n = 0 
i = 0  
#如果i在范围内，i^2在范围内，就删数   
for i in range( 0 , upLimit ):
    #越界，结束
    if ( i + 1 ) ** 2 > upLimit:
        break
    #没越界，但是已经删除过了，就跳过
    if whleList[ i ] == 1 and whleList [ (i+1) ** 2 + n * (i+1) - 1 ] == 0:
        continue
    #还没有删除的数，用循环删掉
    elif whleList[ i ] == 1 and whleList [ (i+1) ** 2 + n * (i+1) - 1 ] == 1:       
        while (i+1) ** 2 + n * (i+1) <= upLimit :
            whleList[ (i+1) ** 2 + n * (i+1) - 1] =  0
            n += 1
    #已经是合数的，跳过
    elif whleList[ i ] == 0:
        pass
    i += 1
    n = 0
    
endTime = time.time()
counter = 0   
#打印所有素数     
for i in range(upLimit):
    if whleList[ i ] == 1:
        print(str(i + 1))
        counter += 1
prtTime = time.time()
#打印时间，总共的素数数
print("the running time is: " + str( endTime - startTime))
print("the printing time is: " + str( prtTime - endTime))
print( "The number of the prime is: " + str( counter ) )