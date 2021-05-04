#include<bits/stdc++.h>
#include "QUEUE.h"

using namespace std;

int main(){
    //Queue to store the database
	myqueue<pair<string,string>> queue;
    //Attributes to be stored
	string name,mobile;
	//Input for menu
	int inp;
	//Try catch block for error handling
	try{
    //Menu
	while(true){
		cout<<"\n\n----MENU---\n";
		cout<<"Enter 1. Add call to database.\n";
		cout<<"Enter 2. Serve a call.\n";
		cout<<"Any any other to exit\n";
		cout<<"\nInput: ";
		cin>>inp;

        //Handling menu cases
		switch(inp){
			case 1:
                //Adding to database
				cout<<"Enter Name: ";
				cin>>name;
				cout<<"Enter Mobile: ";
				cin>>mobile;
				queue.enqueue({name,mobile});
				cout<<"Added to database successfully.\n";
				break;

			case 2:
			    //Serving the data
				if(queue.isEmpty()) cout<<"No calls to Serve.\n";
				else {
                    cout<<"Caller Details\n";
                    cout<<"Name: "<<queue.front().first<<'\n';
                    cout<<"Mobile: "<<queue.front().second<<'\n';
					queue.dequeue();
                    cout<<"Call served successfully.\n";
				}
				break;
			default:
			    //Exiting
			    cout<<"Exiting...";
				return 0;


		}

		}

	}
	catch(const char* err){
		cerr<<"\nError: "<<err;
	}

}
