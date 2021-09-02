#include<bits/stdc++.h>
#define int long long

using namespace std;
/*

Time Complexity : O(m+n) = O(n) -> Linear
Space Complexity : O(m+n) = O(n) -> Linear


Example Input :
1
4 9
10 20 30 40 50 60 70 80 90

Output :
40 30 20 10 50 60 70 80 90 


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

		int m,n; cin>>m>>n;

		stack<int> stack;
		vector<int> queue(n);

		//Inputting m elements to stack
		for(int i=0; i<m; i++){
			int ele;
			cin>>ele;
			stack.push(ele);
		}

		//Rervseing m elements in queue with help of stack
		for(int i=0; i<m; i++){	

			queue[i]=stack.top();
			stack.pop();
		}

		//Rest elements as it is
		for(int i=m; i<n; i++){
			cin>>queue[i];
		}

		//Printing
		for(auto i: queue) cout<<i<<" ";
		cout<<'\n';
		
	}
	return 0;

}
