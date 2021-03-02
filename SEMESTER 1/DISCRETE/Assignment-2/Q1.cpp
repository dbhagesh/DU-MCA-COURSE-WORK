/*
1.Write a recursive program to find the squared sum of N natural numbers
*/
#include<bits/stdc++.h>
using namespace std;
int sqsum(int n,int sum){
    if(n==0) return sum;

    sum+=n*n;
    return sqsum(n-1,sum);
}
int main()
{
    int n;
    cin>>n;

    cout<<sqsum(n,0);
    return 0;

}
