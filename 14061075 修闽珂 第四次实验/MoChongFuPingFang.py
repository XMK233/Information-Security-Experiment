#coding=utf-8
import time
#模重复平房算法
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
#打开文件
outFile = open('output.txt','w')
inFile = open('input.txt','r')

for i in range(10):
    #行输入
    line = inFile.readline()
    #分开数字a,b,n
    a, b, n = line.split()
    a1 = int(a)
    b1 = int(b)
    n1 = int(n)
    #calculating
    strTime = time.time()
    outFile.write( str(mochongfupingfang(a1, b1, n1)) + " ")
    endTime = time.time()
    outFile.write( "the time of mochongfu algorithm is " + str( endTime - strTime) )
    strTime = time.time()
    a1 ** b1 % n1#这里可能会十分久，所以测试数据中没有大数，但是若只用模重复平方就很快
    endTime = time.time()
    outFile.write( " seconds while the time of average algorithm: " + str( endTime - strTime) + " seconds."+'\n')
#showing the statue 
print("executing completes")
#close file
outFile.close()
inFile.close()