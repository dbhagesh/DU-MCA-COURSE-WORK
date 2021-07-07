#include <bits/stdc++.h>
#include "STACK_GROW_TIGHT.h"
using namespace std;
/*
Time complexity : O(n) : As we are traversing on the whole string
Space complexity: O(n/2)=> O(n) : As we are pushing half of the string to the stack.
*/
//Function to check if string is a palindrome or not
bool check_palindrome(string s){
	//Approach: Push half of the string to stack and compare the rest string with the stack
	mystack<char> st;

	//Traversing string
	for(int i=0; i<s.length(); i++){

		//Pushing half string to stack
		if(i<s.length()/2) st.push(s[i]);
		//Comparing rest half string, neglecting the mid element of odd string
		else {
			//Checking for the middle element
			if(!((s.length() & 1) and i==s.length()/2 ))
				//If element not equal therefore its not a palindrome
				if(s[i]!=st.pop()) return false;
		}

	}
	//If comparison successful it is a palindrome
	return true;
}
int main()
{

	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif

	//Number of test cases
	int t;
	cin>>t;

	while(t--){
		//String to check palindrome
		string s;
		cin>>s;
		//Palindrome function
		check_palindrome(s)==0 ? cout<<"Not a palindrome\n": cout<<"Yes, a palindrome.\n";
	}

	return 0;

}
