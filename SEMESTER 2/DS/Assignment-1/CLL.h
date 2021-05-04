using namespace std;
template <class T>
class Node {

	private:
		T data;
		Node<T>* next;

	public:
		//To resolve same template class name
		template<class U>
		//CLL class can access Class Node  members
		friend class CLL;
		//Constructor
		Node(T,Node<T>* node=nullptr);
};

template <class T>
Node<T>::Node(T val, Node<T>* node){
	data = val;
	next = node;
}

template <class T>
class CLL{

	private:
		Node<T>* head; //Head ptr
	public:
		CLL(); //Constructor
		bool isEmpty(); //Function to check if list is empty
		void print(); //FUnction to print the list
		T front(); //Function to return element at the front
		T rear(); //Function to return element at the rear

		void addFront(T ele); //Function to add element at front
		void addBack(T ele); //Function to add element at back

		T removeFront(); //Function to remove element at front
		T removeBack(); //Function to remove element at back

};
template<class T>
CLL<T>::CLL(){
	head=0;
}

template<class T>
bool CLL<T>::isEmpty(){
	return head==0;
}

template<class T>
void CLL<T>::print(){
	if(isEmpty()){
		cout<<"List is Empty.";
		return;
	}

	Node<T>* temp = head;
	cout<<"\nList is: ";
	do{
		cout<<temp->data<<"->";
		temp=temp->next;
	}while(temp!=head);
	cout<<'\n';
}
template<class T>
void CLL<T>::addFront(T data){
	if(head==0){
		head = new Node<T>(data);
		head->next = head;

	}
	else{
		/*
		Inserting at the front is basically
		inserting at the second position and then
		exchanging the data with first node(head)
		*/
		//Inserting at the head
		Node<T>* node = new Node<T>(data);
		node->next = head->next;
		head->next = node;

		//Swapping
		T temp = head->data;
		head->data = node->data;
		node->data = temp;
	}
}
template<class T>
void CLL<T>::addBack(T data){
	if(head==0){
		head = new Node<T>(data);
		head->next = head;

	}
	else{
		/*
		Inserting at the back is basically
		inserting at the second position and then
		exchanging the data with first node(head)
		And making the head point to the second node
		*/
		//Inserting at the head
		Node<T>* node = new Node<T>(data);
		node->next = head->next;
		head->next = node;

		//Swapping
		T temp = head->data;
		head->data = node->data;
		node->data = temp;

		//making head move to next node
		head=head->next;
	}
}

template<class T>
T CLL<T>::removeFront(){
	if(isEmpty())
		throw "List is empty.";
	else if(head->next==head){
		/*
		When only 1 element is present in the list
		We make the head=0 i.e Empty list condition
		*/
		Node<T>* tnode = head;
		T temp = head->data;
		head=0;
		delete tnode;
		return temp;
	}
	else{
		/*
		We cant remove first node directly as i cant make the pointer from last
		node to point to the 2nd node directly.
		So, we copy the data of 2nd node to the 1st node and remove the 2nd node.
		*/
		Node<T>* tnode = head;
		T tdata = head->data;
		head->data = (head->next)->data;
		head->next=(head->next)->next;

		return tdata;

	}

}

template<class T>
T CLL<T>::removeBack(){
	if(isEmpty())
		throw "List is empty.";
	else if(head->next==head){
		/*
		When only 1 element is present in the list
		We make the head=0 i.e Empty list condition
		*/
		Node<T>* tnode = head;
		T temp = head->data;
		head=0;
		delete tnode;
		return temp;
	}
	else{
		/*
		Traversing to the end of the list to delete the
		from the end.
		*/
		Node<T>* tnode = head;
		Node<T>* prev;
		while(tnode->next!=head){
			prev= tnode;
			tnode=tnode->next;
		}
		prev->next = tnode->next;
		T tdata = tnode->data;
		delete tnode;
		return tdata;
	}

}
template<class T>
T CLL<T>::front(){
	if(isEmpty()) throw "List is empty";
	return head->data;
}
template<class T>
T CLL<T>::rear(){
	if(isEmpty()) throw "List is empty";
	Node<T>* temp = head;

	while(temp->next!=head){
		temp=temp->next;
	}
	return temp->data;
}
