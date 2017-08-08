// C++ Program for printing the prime numbers upto n.
// Code started on 03/07/2016
// Last Edit on 04/07/2017
// Code Written by Nabeel Ahmad Khan 


#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<math.h>
#include<cstring>

using namespace std;  //for eliminating the need for writing the standard namespaces like std:cout etc. 

#define FOR(i,a,b) for(int i=a;i<=b;++i)
#define FORD(i,a,b) for(int i=a;i>=b;--i)
#define REP(i,n) FOR(i,0,(int)n-1)
#define MS0(x) memset(x,0,sizeof(x))
#define MS1(x) memset(x,1,sizeof(x))
#define SORT(a,n) sort(begin(a),begin(a)+n)
#define REV(a,n) reverse(begin(a),begin(a)+n)
#define ll long long
#define gc getchar
#define MAX 1000000000

int length(int arr[])   //function for finding the length of an array. 
{
  int count=0;
  int *ptr=&arr[0];
  while(*ptr != '\0')
  {
    ptr++;
    count++;
  }
  return count;
}

int display(int dispArr[])
{
  for(int i=0;i<length(dispArr);i++)
    std::cout<<dispArr[i];
}
 
int checkPrime(int start, int n)  // sieve of eratosthinos for checking prime 
{
    // Create a boolean array "prime[0..n]" and initialize
    // all entries it as true. A value in prime[i] will
    // finally be false if i is Not a prime, else true.
    bool prime[n+1];
    memset(prime, true, sizeof(prime)); //used to initialize values 
 
  prime[1]=false;
    for (int p=2; p*p<=n+1; p++)
    {
        // If prime[p] is not changed, then it is a prime
        if (prime[p] == true)
        {
            // Update all multiples of p
//            int divisorCheck=start/p;
//            if (divisorCheck == 0)
//              divisorCheck=2;
            for (int i=p*2 ; i<=n; i += p)
                prime[i] = false;
        }
    }

    // Print all prime numbers
    for (int p=start; p<=n; p++)
       if (prime[p])
          std::cout << p << "\n";
          
    std::cout<<"\n\n";
}


int main()
{
  int iteration,start,end;
  std::cin >> iteration; //enter the number of iterations you want to run
  for(int i=0;i<iteration;i++)
  {
    std::cin >> start>>end;
    checkPrime(start, end);
  }

  return 0;
}

