#include<bits/stdc++.h>
#define int long long

using namespace std;
int32_t main()
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    #ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	
	int n; cin>>n;
	int arr[n];
	for(auto &i : arr) cin>>i;

	// Largest And Second Largest Element in the array
	// Algo 1 : Sort the array and get the last index
	// Time Complexity : O(nlogn)
	// Space Compleixty : O(1)
	
	sort(arr, arr + n);
	cout<<"Largest Element : "<<arr[n-1]<<endl;
	cout<<"Second Largest Element : "<<arr[n-2]<<endl;

	// Algo 2 : Maintain two variables one for largest and
	// one for second largest
	// Time Complexity : O(n)
	// Space Complexity : O(1)

	int largest, second_largest;
	largest = second_largest = arr[0];

	for(auto i : arr) {
		if(i >= largest) {
			second_largest = largest;
			largest = i;
		}
	}

	cout<<"Largest Element : "<<largest<<endl;
	cout<<"Second Largest Element : "<<second_largest<<endl;


	return 0;

}
