#include<bits/stdc++.h>
#include<cmath>
#include <ctime>
#include <unistd.h>
using namespace std;

//structure for student details
struct Student {
	string name;
	string roll_no;
	string addr;
	string dob;
};

//Dictionary ADT
class dictionary{

	private:
		int curr;//current elements in the table
		int curr1;

		int size;//size of the table

		int insert_lookup;//Lookups
		int search_lookup;
		int delete_lookup;



		vector<vector<struct Student>> v;//Container for chaining
		struct Student *arr;//Container for probing

	public:

	    int del_enteries;//Mainting del_entries for rehashing
	    int del_enteries1;
        //dummy constructor
        dictionary() {}
		dictionary(int);

		//Operations
		void insert_c(int, int, int, Student);
		void search_c(int, int, int, string);
		void delete_c(int, int, int, string);

		//Insertion
		void insert_chain(int,int,Student);
		void insert_linearprobe(int,int,Student);
		void insert_double(int,int,Student);

		//Searching
		void search_chain(int,int,string);
		void search_linearprobe(int,int,string );
		void search_double(int,int,string );

		//Deletion
		void delete_chain(int,int,string );
		void delete_linearprobe(int,int,string );
		void delete_double(int,int,string );

		//Hashcode Map and compression map selection
		int hashcodeMap(string,int);
		int compressionMap(int,int);

		//Hashcode Map
		int componentSum(string);
		int polynomialAcc(string);

		//Compression Map
		int remainder(int);
		int fibonacci(int);
		int mad(int);

		//Universal Hashing
		int universal(string);
		//Rehashing
		void rehashing(int, int, int);

		//Analysis
		void analysis();
};


dictionary::dictionary(int s){
	curr=0;
	curr1=0;

	del_enteries=0;
	del_enteries1=0;
	size = s;

	insert_lookup=0;
	search_lookup=0;
	delete_lookup=0;

	v = vector<vector<struct Student>>(size);
	arr = new struct Student[size];
}


int dictionary:: componentSum(string key){

	int sum=0;
	for(int i=0; i<key.size(); i++){
		sum+=int(key[i]);
	}
	return sum;
}
int dictionary:: polynomialAcc(string key){
	int x = 33;
	int sum=int(key[key.size()-1]);
	for(int i=key.size()-2; i>0; i--){
		sum=int(key[i])+x*sum;
	}
	return sum;
}
int dictionary::hashcodeMap(string key,int c){

	if(c==1)
		return componentSum(key);
	else if(c==2)
		return polynomialAcc(key);
	else
		return universal(key);
}
int dictionary::compressionMap(int key,int c){

	if(c==1) return remainder(key);
	else if(c==2) return fibonacci(key);
	else return mad(key);
}
int dictionary::remainder(int key){
	return key%size;
}
int dictionary::fibonacci(int key){
	//Conjugate of golden ratio
	double A = 0.61803398875;
	double intPart;
	double fracPart = abs(modf(((double)key *A ),&intPart));
	int final = (int)(double(size)*fracPart);
	return final;
}
int dictionary::mad(int key){
	int a = 701;
	int b = 31;
	return abs(a*key + b)%size;
}
void dictionary::insert_chain(int hashcode, int compression,Student obj){

	//hascode mapping
	int int_key = hashcodeMap(obj.roll_no,hashcode);
	//compression mapping
	int key = compressionMap(int_key,compression);

	insert_lookup++;
	v[key].push_back(obj);

}
void dictionary::insert_linearprobe(int hashcode, int compression,Student obj){
	curr1++;

	//hascode mapping
	int int_key = hashcodeMap(obj.roll_no,hashcode);
	//compression mapping
	int key = compressionMap(int_key,compression);
	int probe = key;

	if(curr1 == size){
		cout<<"TABLE FULL\n";
		throw "TABLE FULL EXCEPTION";
	}
	//Current location
	insert_lookup++;
	while(arr[probe].roll_no!="" && arr[probe].roll_no!="DELETED"){
        probe = (probe+1) % size;
        //Checking for more locations
        insert_lookup++;

	}
	//Mainting enteries with DELETED mark
	if(arr[probe].roll_no!="DELETED") del_enteries--;

	arr[probe] = obj;


}
void dictionary::insert_double(int hashcode, int compression,Student obj){
	curr++;
	//hascode mapping
	int int_key = hashcodeMap(obj.roll_no,hashcode);
	//compression mapping
	int key = compressionMap(int_key,compression);

	//Using hashing function for offset as used in the lecture
	//It can be replaced by any hashing function
	int probe = key, offset = (8 - key%8);
	if(curr == size){
		cout<<"TABLE FULL\n";
		throw "TABLE FULL";
	}
	//Current location
	insert_lookup++;
	while(arr[key].roll_no!="" && arr[key].roll_no!="DELETED"){
		key = (key+offset) % size;
		//Checking for more location
		insert_lookup++;
	}

	//Mainting enteries with DELETED mark
	if(arr[key].roll_no!="DELETED") del_enteries1--;

	//Insertion
	arr[key] = obj;


}

void dictionary:: search_linearprobe(int hashcode, int compression,string roll_no){
	//Use the same methods as used for inserting
	//hascode mapping
	int int_key = hashcodeMap(roll_no,hashcode);
	//compression mapping
	int key = compressionMap(int_key,compression);
	//Current lookup;
	search_lookup++;
	while(arr[key].roll_no!="" && arr[key].roll_no!=roll_no){
		key=(key+1)%size;
		//Checking for more locations;
		search_lookup++;

	}
	if(arr[key].roll_no=="") cout<<"NOT FOUND\n";
	else if(arr[key].roll_no==roll_no){
		cout<<"FOUND\n";
        cout<<"Name: "<<arr[key].name<<'\n';
        cout<<"Roll Number: "<<arr[key].roll_no<<'\n';
        cout<<"Address: "<<arr[key].addr<<'\n';
        cout<<"DOB: "<<arr[key].dob<<"\n\n";
	}


}
void dictionary:: search_chain(int hashcode, int compression,string roll_no){
	//Use the same methods as used for inserting
	//hascode mapping
	int int_key = hashcodeMap(roll_no,hashcode);
	//compression mapping
	int key = compressionMap(int_key,compression);

	for(auto chain: v[key] ){
		//Current lookup;
		search_lookup++;
		if(chain.roll_no==roll_no){
			cout<<"FOUND\n";

            cout<<"Name: "<<chain.name<<'\n';
            cout<<"Roll Number: "<<chain.roll_no<<'\n';
            cout<<"Address: "<<chain.addr<<'\n';
            cout<<"DOB: "<<chain.dob<<"\n\n";
			return;
		}
	}
	cout<<"NOT FOUND\n";
}
void dictionary::search_double(int hashcode, int compression,string roll_no){

	//Use the same methods as used for inserting
	//hascode mapping
	int int_key = hashcodeMap(roll_no,hashcode);
	//compression mapping
	int key = compressionMap(int_key,compression);
	int offset = (8 - key%8);

	//Current lookup;
	search_lookup++;
	while(arr[key].roll_no!="" && arr[key].roll_no!=roll_no){

		key=(key+offset)%size;
		//checking for more locations
		search_lookup++;
	}
	if(arr[key].roll_no=="") cout<<"NOT FOUND\n";
	else if(arr[key].roll_no==roll_no){
        cout<<"FOUND\n";
        cout<<"Name: "<<arr[key].name<<'\n';
        cout<<"Roll Number: "<<arr[key].roll_no<<'\n';
        cout<<"Address: "<<arr[key].addr<<'\n';
        cout<<"DOB: "<<arr[key].dob<<"\n\n";
	}

}

void dictionary::delete_chain(int hashcode, int compression,string roll_no){
	//Use the same methods as used for inserting
	//hascode mapping
	int int_key = hashcodeMap(roll_no,hashcode);
	//compression mapping
	int key = compressionMap(int_key,compression);

	for(auto it=v[key].begin(); it!=v[key].end(); it++ ){
		//Current location
		delete_lookup++;
		if(it->roll_no==roll_no){
			v[key].erase(it);
			cout<<"DELETED SUCCESSFULLY\n";
			return;
		}
	}
	cout<<"NOT FOUND\n";

}
void dictionary::delete_linearprobe(int hashcode, int compression,string roll_no){
	//Use the same methods as used for inserting
	//hascode mapping
	int int_key = hashcodeMap(roll_no,hashcode);
	//compression mapping
	int key = compressionMap(int_key,compression);
	///Current lookup;
	delete_lookup++;
	while(arr[key].name!="" && arr[key].roll_no!=roll_no){
		key=(key+1)%size;
		//Looking at furtger locations
		delete_lookup++;
	}
	if(arr[key].name=="") cout<<"NOT FOUND\n";
	else if(arr[key].roll_no==roll_no){
		curr1--;
		del_enteries++;
		arr[key].roll_no="DELETED";
		cout<<"DELETED SUCCESSFULLY\n";
	}
}
void dictionary::delete_double(int hashcode, int compression, string roll_no){
	//Use the same methods as used for inserting
	//hascode mapping
	int int_key = hashcodeMap(roll_no,hashcode);
	//compression mapping
	int key = compressionMap(int_key,compression);

	int offset = (8 - key%8);

	//Current lookup;
	delete_lookup++;

	while(arr[key].name!="" && arr[key].roll_no!=roll_no){
		key=(key+offset)%size;
		//Looking at further locations

		delete_lookup++;
	}
	if(arr[key].name=="") cout<<"NOT FOUND\n";
	else if(arr[key].roll_no==roll_no) {
		curr--;
		del_enteries1++;
		arr[key].roll_no="DELETED";
		cout<<"DELETED SUCCESSFULLY\n";

	}
}

void dictionary::insert_c(int hashcode,int compression,int collision,Student obj){

	if(collision==1){
		insert_chain(hashcode,compression,obj);
	}
	else if(collision==2){
		insert_linearprobe(hashcode,compression,obj);
	}
	else{
		insert_double(hashcode,compression,obj);
	}
}
void dictionary::search_c(int hashcode,int compression,int collision,string roll_no){
	if(collision==1){
		search_chain(hashcode,compression,roll_no);
	}
	else if(collision==2){
		search_linearprobe(hashcode,compression,roll_no);
	}
	else{
		search_double(hashcode,compression,roll_no);
	}
}
void dictionary::delete_c(int hashcode,int compression,int collision,string roll_no){
	if(collision==1){
		delete_chain(hashcode,compression,roll_no);
	}
	else if(collision==2){
		delete_linearprobe(hashcode,compression,roll_no);
	}
	else{
		delete_double(hashcode,compression,roll_no);
	}
}

void dictionary::rehashing(int hashcode, int compression, int collision){
	stack<struct Student> st;

	for(int i=0; i<size; i++){
		if(arr[i].roll_no!="" && arr[i].roll_no!="DELETED" ) st.push(arr[i]);
	}

	while(!st.empty()){
		insert_c(hashcode,compression,collision,st.top());
		st.pop();
	}
}

void dictionary::analysis(){
	cout<<"\n\n--Current Program Analysis-- \n";
	cout<<"Insertion Loopups: "<<insert_lookup<<endl;
	cout<<"Searching Lookups: "<<search_lookup<<endl;
	cout<<"Deletion Lookups: "<<delete_lookup<<endl;
	cout<<"Average : "<<double(insert_lookup+search_lookup+delete_lookup)/3.0<<endl;
	cout<<"------------------------------------------------------------------------------\n";
}

int dictionary::universal(string key){
    insert_lookup++;
    int seed=13;
	vector<int> a;
	for(int i=0; i<key.size(); i++) a.push_back(int(key[i]));

	int int_key=0;
	for(int i=0; i<key.size(); i++){

		int_key+=((seed%size)*int(key[i]))%size;
		int_key=int_key%size;
        seed+=seed;
    }
	return int_key;
}

//Function to assign seed for random input generation
void init(){
	srand( (unsigned) time(NULL) * getpid());
}

//Random text generation
string random_text(int len) {

    string tmp_s;
    static const char alphanum[] =
        "0123456789"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz";

    tmp_s.reserve(len);

    for (int i = 0; i < len; ++i)
        tmp_s += alphanum[rand() % (sizeof(alphanum) - 1)];


    return tmp_s;

}

//Random roll number generation
string random_roll() {

    string tmp_s;
    string course[7]={"MCS","MMA","MMT","PCS","PBA","PMT","MCM"};
    string year[7]={"2021","2020","2019","2018","2017","2016","2015"};

    tmp_s= year[rand() % (6)]+course[rand() % (6)]+to_string(rand() % (10));
    if(tmp_s.size()==8){
    	char tmp = tmp_s[tmp_s.size()-1];
    	tmp_s[tmp_s.size()-1]='0';
    	tmp_s+=tmp;
    }

    return tmp_s;

}

//Input
struct Student input(){
	cout<<"\nInput is taken with the help of random input generator function\n";
	Student obj;
	cout<<"Enter Name: ";
	//cin>>obj.name;
	obj.name = random_text(10);
	cout<<"Enter Roll Number: ";
	//cin>>obj.roll_no;
	obj.roll_no = random_roll();
	cout<<"Enter Address: ";
	//cin>>obj.addr;
	obj.addr = random_text(15);
	cout<<"Enter DOB: ";
	//cin>>obj.dob;
	obj.dob = random_text(6);
	cout<<"\nInserting : "<<obj.roll_no<<endl;
	return obj;
}

int main()
{

    try{
	cout<<"\t\t\t--WELCOME TO THE DICTIONARY--\n\n";
	cout<<"Please note inputs are generated randomly.\n\n";


	cout<<"Choose the Hashcode Map and Compression Map for your dictionary.\n";
	int hashcode,compression,collision,m;



	cout<<"Choose a hashcode Map:\n1.Component Sum\n2.Polynomial Accumulation\n3.Universal Hashing\nNote:By default Universal Hashing\n\n";
	cout<<"Enter: ";
	cin>>hashcode;

	cout<<"Choose a compression Map:\n";
	cout<<"1.Use remainder(h(k)=k mod m) \n";
	cout<<"2.Fibonacci Hashing\n";
	cout<<"3.Using Multiply, Add and Divide\n";
	cout<<"By default last one will be selected\n\n";
	cout<<"Enter: ";
	cin>>compression;

	cout<<"\n\nChoose Type of Collision Resolution: ";
	cout<<"\n1.Chaining";
	cout<<"\n2.Linear Probing";
	cout<<"\n3.Double Hashing\n";
	cout<<"Enter: ";
	cin>>collision;

	cout<<"\nEnter the size of the dictionary: ";
	cin>>m;

	dictionary d(m);

    string roll_no;
    Student s;
	while(true){

		cout<<"\n\n\n\t\t\t\t\t\t--MENU--\n\n";
		cout<<"\t1. Insert \n";
		cout<<"\t2. Search \n";
		cout<<"\t3. Delete \n";
		cout<<"\tElse Analysis and exit \n\n";
		int choice;
        cout<<"\tEnter: ";
        cin>>choice;
        cout<<"\n\n";

        if(2*d.del_enteries>=m )
        	d.rehashing(hashcode,compression,collision);


		switch(choice){

			case 1:
                s = input();
				d.insert_c(hashcode,compression,collision,s);
				break;

			case 2:
				cout<<"Enter Roll Number to search: ";
				cin>>roll_no;
				d.search_c(hashcode,compression,collision,roll_no);
				break;

			case 3:

				cout<<"Enter Roll Number to delete: ";
				cin>>roll_no;
				d.delete_c(hashcode,compression,collision,roll_no);
				break;

			default:
                d.analysis();
				cout<<"Exiting Program...\n\n";

				return 0;

		}
	}



}catch(const char * err){
	cerr<<err;
}



	return 0;

}

