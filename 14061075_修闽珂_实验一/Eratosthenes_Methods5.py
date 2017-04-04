import  math, time 

upLimit = int(input ("input range: "))
#计算10以内的素数，这个是后续计算的基础
num = [1]
whleList = [1] * 10
whleList [ 0 ] = 0#
for i in range (2, 11):
    for j in range(2, i):
        if (i ) % j == 0:
            whleList [i-1] = 0
num *= (upLimit - 10)
whleList += num        

#主要的函数
def findPrime(sqrtLimit):
    #如果范围太大，就开方并递归
    if sqrtLimit > 10:
        sqrtLimit = int(math.sqrt(sqrtLimit)) 
        findPrime(sqrtLimit)
    #删数，只要在开方的范围内是质数的，其在开方的范围以外的部分是i的倍数的都删掉
    for i in range ( sqrtLimit):
        if whleList[ i ] == 1:
            #n = 0''' '''#
            for j in range (sqrtLimit, len(whleList) ):
                if (j + 1) % (i + 1) == 0 and whleList [ j ] != 0: 
                    whleList [ j ] = 0
        else:
            pass
        
def main():
    #范围
    sqrtLimit = upLimit
    #时间
    strTime = time.time()
    #运行功能函数
    findPrime(sqrtLimit)
    endTime = time.time()
    counter = 0
    #打出素数并计算素数的数量
    for i in range(upLimit):
        if whleList [ i ] == 1:
            print( str( i + 1))
            counter += 1 
    prtTime = time.time()
    #打出时间和素数个数
    print ( "the number is : " + str (counter))   
    print ( "the counting time is : " + str (endTime - strTime))  
    print ( "the printing time is : " + str (prtTime - endTime))
        
if __name__ == '__main__':
    main()
    
    
            
           
            
    
