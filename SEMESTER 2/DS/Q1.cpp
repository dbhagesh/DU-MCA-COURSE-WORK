/*
Give an array consisting of only two elements 'a' and 'b'.
Arrange the array so that all the a's come before all the b's in O(n) time and O(1) additional space
User - Bhagesh
Approach - Counting number of a's 
Time Complexity -  
Please note: first while loop is just for running the 
logic on different test cases

Logic: 
Input in array : O(n)
Second for loop : O(n)
                 _____________
                 O(2*n) = O(n)

Space Complexity = O(1)
As our program takes the same amount of space regardless of the input size
				  
*/
#include<bits/stdc++.h>

using namespace std;
int main()
{
	

    #ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	//size of array
	int t,n,c1=0;
	//Number Test cases
	cin>>t;

	//Loop for test cases
	while(t--){
		cin>>n;
		//array
		char arr[n];

		//counting
		for(auto &i: arr){
		cin>>i;
		if(i=='a') c1++;

		}
		//changing the array and outputing it
		for(int i=0; i<n; i++){
		if(c1 >0) c1--,arr[i]='a';
		else arr[i]='b';

		cout<<arr[i]<<" ";
		}
		cout<<'\n';
		cout<<"-------------\n";

	
	}
	return 0;	
	

}
