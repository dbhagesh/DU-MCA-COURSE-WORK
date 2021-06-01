#include<bits/stdc++.h>
//ADT
#include "STACK.h"

using namespace std;

int main()
{

	//Number of test cases
	int t;
	cin>>t;



	//Running over test cases
	while(t--){
		//Input string
		//Flushing standard input for reading emty string
		fflush(stdin);
        cin.clear();
		string s;


		getline(cin,s);
		cout<<"STRING IS : "<<s<<endl;


		//mystack ADT
		mystack<char> st;
		//Flags for emptystack and wrong character input other than a and b
		int emptyflag=1,wrongCharFlag=0;

		//Traversing over string
		for(int i=0; i<s.size(); i++){
			//If char is 'a' push to stack
			if(s[i]=='a') st.push(s[i]);
			//If char is 'b' pop from the stack
			else if(s[i]=='b'){
				//If nothing to pop for 'b'
				if(st.size()==0)
				{
					emptyflag=0;
					break;
				}
				//If stack top is 'a' pop it
				else if(st.top()=='a') st.pop(); //If top is 'a'
			}
			//If wrong character in input
			else{
                wrongCharFlag=1;
                break;
			}


		}
		cout<<"OUTPUT: ";
		//If stack got empty after traversing on whole string and if wrongCharacter isnt present in input
		if((st.size()==0 and emptyflag==1) and wrongCharFlag==0 ) cout<<"TRUE\n";
		//If stack isnt empty or if stack went empty in between of traversing the string
		else cout<<"NO\n";

	}
	return 0;

}
