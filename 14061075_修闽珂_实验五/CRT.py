#coding=utf-8
#woshishei
def chenglv(b, a):#乘率的算法
    b = b % a  
    tempa = a
    q = []
    n = 0
    while 1:
        temp = int(a / b)
        mod = a % b
        a = b
        b = mod
        if b:
            q.append(temp)#把商数收集起来
            n += 1
        else:   
            break
    c = []
    c.append(1)
    if q != []:
        c.append(q[0])
    else:
        return 1
    for i in range(2,n+1):
        c.append(q[i - 1] * c[i - 1] + c[i - 2])#c是乘率的列表，最有一个就是所求乘率。通项公式就是这一行所显示的
    tempfin = ((-1)**n)*c[len(c) - 1]
    if tempfin > 0:
        return  tempfin
    elif tempfin < 0:
        return tempfin + tempa
'''def chenglv(b, a):#这种方法可以不要用列表来储存，但是没办法完成两步之内就结束的计算过程，两步以上方可执行。功能与上述函数毫无区别。
    n = 0
    c0 = 1
    temp = a
    c2 = 0
    while 1:
        q = int(a / b)
        mod = a % b
        a = b
        b = mod
        if b == 0:
            if n == 0:
                return 1
            break
        if n == 0:
            c1 = q 
            n += 1
        else:
            c2 = q * c1 + c0
            c0 = c1
            c1 = c2
            n += 1
    tempfin = ((-1)**n)*c2 
    if tempfin > 0:
        return  tempfin
    elif tempfin < 0:
        return tempfin + temp
'''
if __name__ == '__main__' :
    fileIn = open("input.txt", "r")
    fileOut = open("output.txt","w")
    b = []#余数集
    mi = []#除数集
    n = int(fileIn.readline())#个数
    x = 0#原答数
    m = 1#原最小公倍数
    MI = 0#衍数
    #
    for i in range(n):
        k = fileIn.readline()
        a, t = k.split()
        
        b.append( int(a) )#录入余数和除数
        mi.append( int(t) )
        m *= int( t )
    #
    for i in range(n):
        MI = int(m // mi[ i ])#
        x += MI * chenglv(MI, mi[ i ]) * b[ i ]#求答数的过程
    x = x % m#最终答数
    #
    fileOut.write(str( int(x) ) + " " + str(m))
    #
    fileIn.close()
    fileOut.close()
    print(str( int(x) ) + " " + str(m))
    
    
    
    
    
    
    