#include<bits/stdc++.h>
using namespace std;
/*
Time complexity: O(n) per test case: As we traverse the whole string
Space complexity: O(n) as in the worst case we need to push all the string on the stack
*/
//Returns true on balanced paranthesis and false on invalid paranthesis
bool check_bal_parenthesis(string s){
	//stack
	stack<char> st;

	//traversing
	for(int i=0; i<s.length(); i++){

		//if opening braces
		if(s[i]=='{' or s[i]=='[' or s[i]=='(') st.push(s[i]);
		//if closing braces , check if top isnt same as the opening part or stack doesnt
		//contain the opening part then return false else pop the opning part of the closing

		else if(s[i]=='}'){

			if(st.empty() or st.top()!='{') return false;
			else st.pop();
		}
		else if(s[i]==')'){

			if(st.empty() or st.top()!='(') return false;
			else st.pop();
		}
		else if(s[i]==']'){

			if(st.empty() or st.top()!='[') return false;
			else st.pop();
		}



	}
	//If stack empty then true
	return st.size()==0;
}
int main()
{
  
	//Specifying number of test cases
	int t;
	cin>>t;
	while(t--){
		//String generated by compiler
		string s;
		cin>>s;
		//Calling our check balanced paranthesis function
		cout<<check_bal_parenthesis(s)<<endl;
	}

	return 0;

}