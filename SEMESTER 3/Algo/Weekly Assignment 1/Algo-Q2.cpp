#include<bits/stdc++.h>
#define int long long

using namespace std;
/*

Time Complexity : O(n) -> Linear
Space Complexity : O(n) -> Linear


Example Input :
1
9
20 6 5 10 11 -3 -2 5 4

Output :
true

*/


int32_t main()
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    #ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	int t;

	cin>>t;

	while(t--){

		int n,ele; cin>>n;
		stack<int> stack;

		//Pushing in order to stack 20 6 5 10 11 -3 -2 5 4
		//To get this order 4 5 -2 -3 11 10 5 6 20

		//Pushing to stack
		for(int i=0; i<n; i++){

			cin>>ele;
			stack.push(ele);

		}

		//Initially ans=true
		bool ans = true;

		/*
		
		--------Working---------
		
		stack.size()=9
		If we cant pop out 2 elements from the stack that means
		our task is done
		If even elements : all the elements would be popped out and treated
		If odd elements :  every element leaving behind last element will be treated
	
		After popping two elements 

		We check if absolute value of there difference is not equal to 1. Then the answer
		turns "false".
		If no such situation was arised then the answer remains "true".
		
		E.g

		Stack : 4 5 -2 -3 11 10 5 6 20
		a = 4 b = 5
		abs diff == 1
		ans=true

		------------------------------

		Stack : -2 -3 11 10 5 6 20
		a = -2 b = -3
		abs diff == 1
		ans=true
		
		------------------------------

		Stack : 11 10 5 6 20
		a = 11 b = 10
		abs diff == 1
		ans=true

		------------------------------

		Stack : 5 6 20
		a = 5 b = 6
		abs diff == 1
		ans=true

		
		------------------------------

		Stack : 20
		As stack size<2 while loop ends
		ans=true

		Final ans = true

		*/



		//Popping top two elements from the stack
		while(stack.size()>=2){

			int a = stack.top();
			stack.pop();

			int b = stack.top();
			stack.pop();

			if(abs(a-b)!=1) ans=false;

		}

		cout<<(ans ? "true" : "false")<<endl;


		
		
	}
	return 0;

}
