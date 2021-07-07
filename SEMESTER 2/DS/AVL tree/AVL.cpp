#include<bits/stdc++.h>
using namespace std;

//AVL NODE
struct node
{
	int data;
	struct node *left;
	struct node *right;
}*root;

//AVL class
class AVL
{
public:
	//Height of tree
	int height(node *);
	//Difference of height left and right subtree
	int diff(node *);

	//Rotations
	node *right_right(node *);
	node *left_left(node *);
	node *left_right(node *);
	node *right_left(node *);

	//Balancing
	node* balance(node *);

	//Insertion
	node* insert(node *, int);

	//Display
	void display(node *, int);

	//Deletion
	node* remove(node* t, int x);

	//Min and max
	node* find_min(node*);
	node* find_max(node*);

	//Constructor
	AVL()
	{
		root = NULL;
	}
};


// Height of AVL Tree
int AVL::height(node *temp)
{
	int h = 0;
	if (temp != NULL)
	{
		int left_subtree_height = height(temp->left);
		int right_subtree_height = height(temp->right);
		int max_height = max(left_subtree_height, right_subtree_height);
		h = max_height + 1;
	}
	return h;
}

//Height Difference
int AVL::diff(node *temp)
{
	int left_subtree_height = height(temp->left);
	int right_subtree_height = height(temp->right);
	int height_factor = left_subtree_height - right_subtree_height;
	return height_factor;
}

// Rotaions
// ->  right-right
// ->  left-left
// ->  left-right
// ->  right-left

node *AVL::right_right(node *parent)
{
	node *temp;
	temp = parent->right;
	parent->right = temp->left;
	temp->left = parent;
	return temp;
}

node *AVL::left_left(node *parent)
{
	node *temp;
	temp = parent->left;
	parent->left = temp->right;
	temp->right = parent;
	return temp;
}


node *AVL::left_right(node *parent)
{
	node *temp;
	temp = parent->left;
	parent->left = right_right(temp);
	return left_left(parent);
}


node *AVL::right_left(node *parent)
{
	node *temp;
	temp = parent->right;
	parent->right = left_left(temp);
	return right_right(parent);
}

//Balancing AVL Tree
node *AVL::balance(node *temp)
{
	int balalance_factor = diff(temp);

	//Left subtree
	if (balalance_factor > 1)
	{
		//Left subtree
		if (diff(temp->left) > 0)
			temp = left_left(temp);
		//Right subtree
		else
			temp = left_right(temp);
	}
	//Right subtree
	else if (balalance_factor < -1)
	{
		//Left subtree
		if (diff(temp->right) > 0)
			temp = right_left(temp);
		//Right subtree
		else
			temp = right_right(temp);
	}
	return temp;
}

//Insertion
node *AVL::insert(node *root, int value)
{
	if (root == NULL)
	{
		root = new node;
		root->data = value;
		root->left = NULL;
		root->right = NULL;
		return root;
	}
	else if (value < root->data)
	{
		root->left = insert(root->left, value);
		root = balance(root);
	}
	else if (value >= root->data)
	{
		root->right = insert(root->right, value);
		root = balance(root);
	}
	return root;
}

//Display
void AVL::display(node *ptr, int level)
{
	int i;
	if (ptr != NULL)
	{
		display(ptr->right, level + 1);
		cout<<'\n';
		if (ptr == root)
			cout << "Root -> ";
		for (i = 0; i < level && ptr != root; i++)
			cout << "        ";
		cout << ptr->data;
		display(ptr->left, level + 1);
	}
}

node* AVL::find_min(node* t) {
	//If no left node
	if (t == NULL) return NULL;
	//If max left
	else if (t->left == NULL) return t;
	//Recursive call
	else return find_min(t->left);
}
node* AVL:: find_max(node* t) {
	//If no leaf node
	if (t == NULL) return NULL;
	//If max right
	else if (t->right == NULL) return t;
	//Recursive call
	else return find_max(t->right);
}

node* AVL:: remove(node* t, int ele) {
	node* temp;
	// Element not present
	if (t == NULL){
        cout<<"Element not present"<<'\n';
        return NULL;
	}
	// In left subtree
	else if (ele < t->data){
		t->left = remove(t->left, ele);
	}
	// In right subtree
	else if (ele >t->data){
		t->right = remove(t->right, ele);
	}
	// With 2 children case
	else if (t->left && t->right) {
		temp = find_min(t->right);
		t->data = temp->data;
		t->right = remove(t->right, t->data);
	}
	// With 1 or 0 child case
	else {
		temp = t;
		if (t->left == NULL) t = t->right;
		else if (t->right == NULL) t = t->left;
		delete temp;
		cout<<"Deleted Successfully."<<'\n';
	}

	if (t == NULL){

        return t;
	}
	// Balance Check
	t = balance(t);
}



int main()
{
	int input, value;
	AVL avl;
	while (1)
	{
		cout << "\n--------------------------" << endl;
		cout << "       < AVL Tree >      " << endl;
		cout << "\n--------------------------" << endl;
		cout << "1.Insert" << endl;
		cout << "2.Delete" << endl;
		cout << "3.Display" << endl;
		cout << "4.Exit" << endl;
		cout << "Enter your input: ";
		cin >> input;
		cout<<endl;
		switch (input)
		{
		case 1:
			cout << "Enter value to be inserted: ";
			cin >> value;
			root = avl.insert(root, value);
			break;

		case 2:
		    if (root == NULL)
			{
				cout << "Tree is Empty" << endl;
				continue;
			}
			cout << "Enter value to be deleted: ";
			cin >> value;

			root = avl.remove(root, value);

			break;

		case 3:
			if (root == NULL)
			{
				cout << "Tree is Empty" << endl;
				continue;
			}
			cout << "Balanced AVL Tree:" << endl;
			avl.display(root, 1);
			break;

		case 4:
			exit(1);
			break;

		default:
			cout << "Wrong input" << endl;
		}
	}
	return 0;
}
