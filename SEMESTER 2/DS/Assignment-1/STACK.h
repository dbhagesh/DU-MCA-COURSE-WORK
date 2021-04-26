#include "CLL.h"
using namespace std;
template<class E>
class mystack{
	private:
		//Using the ADT defined in CLL.h header file
		CLL<E> list;
		//To store the size of the stack
		int capacity;

	public:
		mystack(); // COnstructor
		int size();// Returns the number of elements in the stack
		bool isEmpty();	//check if stack is empty
		void push(E ele); // push to the top of stack
		E pop();//pop the top of the stack and returns the popped element
		E top();//returns the element at the top of the stack
};

template<class E>
mystack<E>::mystack(){
	capacity=0;
}

template<class E>
int mystack<E>:: size(){
	return capacity;
}

template<class E>
bool mystack<E>::isEmpty(){
	return list.isEmpty();
}

template<class E>
void mystack<E>::push(E ele){
	//Increasing the capacity on every push
	capacity++;
	list.addBack(ele);
}

template<class E>
E mystack<E>::pop(){
	//Decreasing the capacity on every pop
	capacity--;
	//Capacity cant be negative
	if(capacity<0) capacity=0;
	return list.removeBack();
}
template<class E>
E mystack<E>::top(){
	return list.rear();
}
