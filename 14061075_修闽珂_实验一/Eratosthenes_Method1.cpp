#include <iostream> 
#include <stdlib.h>
#include <time.h>
int main()
{
	using namespace std;
	int upLimit = 0;
	cout << "enter the range: " ;
	cin >> upLimit;	
	int  * whleList = new int [upLimit];// the list of the prime, the index in this array whose value plus 1 is the prime we want 
	time_t t_start,t_end, t_print;//time index
	/*int *point1, * point2;*/
	/*point1 = point2 = whleList;*/
	/**/
	t_start = time(NULL) ;	
	for ( int i = 0; i< upLimit; i++ ){
		whleList[ i ] = 1;
	}// fill the array using 1; if it is prime the value remains 1 otherwise it will convert into 0
	whleList[0] = 0;// the first one represent the 1 is not a prime so the value is 0
	
	int n=0, i = 0; 
	for ( i=0; i<upLimit; i++){ // from now on we begin to find the prime.
	
		if ((i + 1) * ( i + 1 ) > upLimit){// the range is overflowing the range, break, it should have been placed in front of calculating function part but I
			break; // placed it behind that so I crashed once. But with God's help I correct the error.
		}
		
		if (whleList[ i ] == 1 && whleList [ ( i + 1) * ( i + 1 ) + n * (i + 1 ) - 1] == 0){//using the eratosthenes algorithm
			continue;// already deleted
		} 
		else if (whleList[ i ] == 1 && whleList [ (i+1) * ( i  + 1) + n * (i+1) - 1 ] == 1){// haven't been deleted
			while (( i + 1 ) * ( i + 1) + n * ( i + 1 ) <= upLimit) {// iteration of deleteing 
            	whleList[ (i+1) * ( i  + 1) + n * (i+1) - 1] =  0;
            	n += 1;
            }
		}
		else if (whleList [ i ] == 0){
			 ; 
		}
		
		n = 0;
		
	}
	//print all the primes and count the time consumed
	t_end = time(NULL) ;
	int  counter = 0;
	for (i = 0, counter = 0; i < upLimit; i++){
		if ( whleList [ i ] == 1){
			//cout << i+1 << '\n' ;//printing is taking an enormous amount of time so I just write it into notes
			counter++;
 		}
	}
	//
	t_print = time(NULL) ;
	cout <<	"the number is: " << counter << '\n';
	cout << "the time is: " << difftime(t_end,t_start) << " s \n";
	delete [] whleList;
	system("pause");
	return 0; 
		
}
