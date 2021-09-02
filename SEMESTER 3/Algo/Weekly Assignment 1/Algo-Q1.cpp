#include<bits/stdc++.h>
#define int long long

using namespace std;

/*

Time Complexity : O(n) -> Linear
Space Complexity : O(n) -> Linear


Example Input :
2
6
30 20 50 60 40 10
6
10 50 40 60 30 20

Output :
AAABBAABABBB
ABAAAABBABBB


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
		
		int n; cin>>n;

		int ele[] = {10,20,30,40,50,60};
		int order[n];
		stack<int> stack;
		vector<char> ans;

		for(auto &i: order) cin>>i;

		
		/*

		Task : To Pop out elements strored in order array and print the queires made to stack
		Input : 30 20 50 60 40 10
		
		Pushing 3 elements to reach 30 -> i=3
		10 20 30 AAA
		
		Popping top 2 elements from stack -> i=3,k=2
		30 20 BB
		
		Pushing next to elements to reach 50 -> i=5,k=2
		40 50 AA

		Pop 50 ->i=5,k=3
		50 B

		Pushing 60 ->i=6,k=3
		60 A

		Pop 60 -> i=6,k=4
		60 B

		Pop 60 -> i=6,k=5
		40 B

		Pop 60 -> i=6,k=6
		10 B
		
		Done!!
		---------------------------

		Input : 10 50 40 60 30 20

		10 A
		10 B
		20 30 40 50 AAAA
		50 40 BB
		60 A
		30 B
		20 B
		*/

		//order var
		int k=0;

		for(int i=0; i<n or k<n; i){

			if(!stack.empty() and stack.top()==order[k]){
				stack.pop();
				ans.push_back('B');
				k++;
			}
			else{
				stack.push(ele[i]);
				ans.push_back('A');
				i++;
			}
		}

		for(auto i: ans) cout<<i;
		cout<<endl;

		
	}
	return 0;

}
