#include <bits/stdc++.h>
#define DEFAULTSIZE 10
using namespace std;

template<class T>
class mystack{
	private:
		T *arr; //Dynamic array
		int top; //Pointer to maintain top of the stack
		int capacity; //Variable to hold size of size of the stack
		int c; //For tight strategy

	public:
		mystack(int size = DEFAULTSIZE); //Constructor
		int size(); //Returns the current number of elements in the stack
		bool isEmpty(); //Returns true if empty
		bool isFull(); //Returns true if full
		void push(T ele); //Push to the stack with tight strategy for growing
		T peek(); //Returns the element at top of the stack
		T pop(); //Pops the element at top
		void display(); //Display the stack

};

template<class T>
mystack<T>::mystack( int size){
	capacity = size;
	c = capacity;
	arr = new T[capacity];
	top = -1;
}

template<class T>
int mystack<T>::size(){
	return top+1;
}

template<class T>
bool mystack<T>::isEmpty(){
	return top==-1;
}

template<class T>
bool mystack<T>::isFull(){
	return ((top+1)==capacity);
}

template<class T>
T mystack<T>::peek(){
	if(isEmpty())
		throw "Stack is Empty.";
	return arr[top];
}

template<class T>
T mystack<T>::pop(){
	if(isEmpty())
		throw "Stack is Empty.";

	return arr[top--];
}

template<class T>
void mystack<T>::push(T ele){
	if(isFull()){

		int newSize = capacity+c;
		T *newArr = new T[newSize];
		for(int i=0;i<capacity; i++){
			newArr[i]=arr[i];
		}
		arr = newArr;
		capacity = newSize;


	}


	arr[++top] = ele;


}

template<class T>
void mystack<T>::display(){

	int t = top+1;
	cout<<"\n\n-----STACK TOP-----\n";
	while(t--){
		cout<<'\t'<<'\t'<<arr[t]<<'\n';
	}

	cout<<"-----STACK BOTTOM-----\n\n";
}
