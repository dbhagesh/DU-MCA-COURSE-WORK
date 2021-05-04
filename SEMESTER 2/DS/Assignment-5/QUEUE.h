
#include<bits/stdc++.h>
#include "CLL.h"
using namespace std;

template<class E>
class myqueue{
	private:
		//Using the ADT defined in CLL.h header file
		CLL<E> list;
		//To store the size of the queue
		int capacity;

	public:
		myqueue(); // COnstructor
		int size();// Returns the number of elements in the queue
		bool isEmpty();	//check if queue is empty
		void enqueue(E ele); // push to the back of queue
		void dequeue();//pop the front of the queue
		E front();//returns the element at the front of the queue

};

template<class E>
myqueue<E>::myqueue(){
	capacity=0;
}

template<class E>
int myqueue<E>:: size(){
	return capacity;
}

template<class E>
bool myqueue<E>::isEmpty(){
	return list.isEmpty();
}

template<class E>
void myqueue<E>::enqueue(E ele){
	//Increasing the capacity on every push
	capacity++;
	list.addBack(ele);
}

template<class E>
void myqueue<E>::dequeue(){
	if(isEmpty()) throw "Queue Empty";
	//Decreasing the capacity on every pop
	capacity--;
	//Capacity cant be negative
	if(capacity<0) capacity=0;
	E temp = list.removeFront();
}
template<class E>
E myqueue<E>::front(){
	if(isEmpty()) throw "Queue Empty";
	return list.front();
}
