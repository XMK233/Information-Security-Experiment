import time

upLimit = int(input ("input range: "))

#�����е�����Ԫ��ͳͳ���ó�1����һ������Ϊ�㣬��Ϊ1��������
startTime = time.time()
whleList = [1] * upLimit
whleList[ 0 ] = 0

n = 0 
i = 0  
#���i�ڷ�Χ�ڣ�i^2�ڷ�Χ�ڣ���ɾ��   
for i in range( 0 , upLimit ):
    #Խ�磬����
    if ( i + 1 ) ** 2 > upLimit:
        break
    #ûԽ�磬�����Ѿ�ɾ�����ˣ�������
    if whleList[ i ] == 1 and whleList [ (i+1) ** 2 + n * (i+1) - 1 ] == 0:
        continue
    #��û��ɾ����������ѭ��ɾ��
    elif whleList[ i ] == 1 and whleList [ (i+1) ** 2 + n * (i+1) - 1 ] == 1:       
        while (i+1) ** 2 + n * (i+1) <= upLimit :
            whleList[ (i+1) ** 2 + n * (i+1) - 1] =  0
            n += 1
    #�Ѿ��Ǻ����ģ�����
    elif whleList[ i ] == 0:
        pass
    i += 1
    n = 0
    
endTime = time.time()
counter = 0   
#��ӡ��������     
for i in range(upLimit):
    if whleList[ i ] == 1:
        print(str(i + 1))
        counter += 1
prtTime = time.time()
#��ӡʱ�䣬�ܹ���������
print("the running time is: " + str( endTime - startTime))
print("the printing time is: " + str( prtTime - endTime))
print( "The number of the prime is: " + str( counter ) )