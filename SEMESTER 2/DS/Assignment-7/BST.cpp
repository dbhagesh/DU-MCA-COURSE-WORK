#include<bits/stdc++.h>
#include<cmath>
#include <ctime>
#include <unistd.h>
using namespace std;

struct Node {

  int data;     // data
  Node* left;   // left pointer
  Node* right;  // right pointer
  Node* ptr; //parent node


  Node(int data1, Node *ptr1 = nullptr, Node* left1 = nullptr, Node* right1 = nullptr) {

    data = data1;
    left = left1;
    right = right1;
    ptr = ptr1;
  }

};

class BST {


  public:
  Node* root;  // BST root node

  Node* insertRec(Node*, int);          // Recursively Insert a node to BST
  Node* deleteByCopying(Node*, int);  // delete a BST node by copying mechanism


  void inorderR(Node*) ;         // Recursive Inorder traversal of tree
  void preorderR(Node*) ;        // Recursive Preorder traversal of tree
  void postorderR(Node*) ;       // Recursive Postorder traversal of tree
  void eulerTour(Node*);         // Euler Tour Recursive traversal of tree
  void eulerTourHelp();          // Euler Tour Helper traversal of tree

  Node* findR(Node*, int) ;      // Recursively find a node in BST
  Node* minValueNode(Node*) ;    // Find min value node in a subtree
  Node* getSuccessor(Node*) ;    // find successor for a node
  Node* maxValueNode(Node*) ;    // Find max value node in a subtree
  Node* getPredecessor(Node*);  // find predecessor for a node


  BST(Node*);  // acts as default as well as parameterized ructor


  Node* getRoot();         // obtain root of Tree (sometimes needed)
  void insertNode(int);    // inserts a Node to BST
  void deleteNode(int);    // deletes a Node from BST
  Node* find(int) ;   // finds a node in BST and returns a pointer to it
  void inorder() ;    // inorder traversal of the BST
  void preorder() ;   // preorder traversal of the BST
  void postorder() ;  // postorder traversal of the BST

};


BST::BST(Node* _root = nullptr){ root = _root; }


//BST::~BST() { deleteTree(root); }

void BST::eulerTourHelp(){ eulerTour(root);}
void BST::eulerTour(Node *root) {

  if(root==nullptr){

  }
  else if (root->left==nullptr and root->right==nullptr) {
    cout<<root->data<<" ";

  }
  else{
    cout<<root->data<<" ";
    eulerTour(root->left);
    cout<<root->data<<" ";
    eulerTour(root->right);
    cout<<root->data<<" ";
  }


}
Node* BST::getRoot() { return root; }

void BST::insertNode(int data) { root = insertRec(root, data); }
Node* BST::insertRec(Node* root, int data) {

  Node *temp;
  if (root == nullptr) {
    root = new Node(data);
    root->left=nullptr;
    root->right=nullptr;

  }
  else if (data <= root->data) {
    temp = insertRec(root->left, data);
    root->left = temp;
    temp->ptr = root;

  } else {
    temp = insertRec(root->right, data);
    root->right = temp;
    temp->ptr = root;
  }
  return root;
}

void BST::deleteNode(int key) { root = deleteByCopying(root, key); }
Node* BST::deleteByCopying(Node* root, int key) {
  /*
  In case 1 : simply delete the node
  In case 2 : the parent adopts the child of target
  In case 3 : Copy the successor/ predecssor to the target node & then delete
  the successor/predecessor
  */

  if (root) {
    // target is from root->left subtree
    if (key < root->data) {
      root->left = deleteByCopying(root->left, key);
    }

    // target is from root->right subtree
    else if (key > root->data) {
      root->right = deleteByCopying(root->right, key);
    }

    // target is root
    else if (key == root->data) {
      // Handles : No child & right child
      if (root->left == nullptr) {
        Node* target = root;
        root = root->right;
        delete target;
      }

      // Handles : No child & left child
      else if (root->right == nullptr) {
        Node* target = root;
        root = root->left;
        delete target;
      }

      // Handles : two child case
      else {
        // using successor
        Node* successor = getSuccessor(root);
        root->data = successor->data;
        root->right = deleteByCopying(root->right, successor->data);

        // using predecessor
        // Node* predecessor = maxValueNode(root->left);
        // root->data = predecessor->data;
        // root->left = deleteByCopying(root->left, predecessor->data);
      }
    }
  }

  return root;
}


void BST::inorder()  { inorderR(root); }
void BST::inorderR(Node* root)  {

  if (root) {
    inorderR(root->left);
    cout << root->data << "  ";
    inorderR(root->right);
  }
}

void BST::preorder()  { preorderR(root); }
void BST::preorderR(Node* root)  {

  if (root) {
    cout << root->data << "  ";
    preorderR(root->left);
    preorderR(root->right);
  }
}

void BST::postorder()  { postorderR(root); }
void BST::postorderR(Node* root)  {

  if (root) {
    postorderR(root->left);
    postorderR(root->right);
    cout << root->data << "  ";
  }
}


Node* BST::find(int key)  { return findR(root, key); }
Node* BST::findR(Node* root, int key)  {

  if (!root) {
    return nullptr;
  }

  if (root->data == key) {
    return root;
  } else if (key < root->data) {
    return findR(root->left, key);
  } else {
    return findR(root->right, key);
  }
}

Node* BST::getSuccessor(Node* root) {

    if(root->right!=nullptr)
        return minValueNode(root->right);

    Node *p = root->ptr;
    while(p!=nullptr and root==p->right){
        root = p;
        p = p->ptr;
    }
    return p;

}
Node* BST::minValueNode(Node* root)  {

  Node* min = root;
  while (min->left) {
    min = min->left;
  }
  return min;
}

Node* BST::getPredecessor(Node* root) {
  if(root->left!=nullptr)
    return maxValueNode(root->left);
  Node *p = root->ptr;
  while(p!=nullptr and root==p->left){
    root = p;
    p = p->ptr;
  }
  return p;
}
Node* BST::maxValueNode(Node* root)  {

  Node* max = root;
  while (max->right) {
    max = max->right;
  }
  return max;
}
void init(){
  srand( (unsigned) time(NULL) * getpid());
}
int random_input(int n) {

  int tmp;

  tmp= rand() % (n);

  return tmp;

}

int main() {
  BST tree;
  init();
  int inp;
  while(true){
    int key;
    Node* result;
    cout<<"\n\n------BST------\n\n";
    cout<<"\n1. Insert";
    cout<<"\n2. Search";
    cout<<"\n3. Delete";
    cout<<"\n4. Traversal General";
    cout<<"\n5. Traversal Specialized";
    cout<<"\n6. Max";
    cout<<"\n7. Min";
    cout<<"\n8. Predecessor";
    cout<<"\n9. Successor";
    cout<<"\n Exit on any other input\n\n";
    cin>>inp;

    switch(inp){

      case 1:
        int num,range;
        cout<<"\nEnter number of inputs to insert : ";
        cin>>num;
        cout<<"\nEnter the range in which inputs should be given : ";
        cin>>range;

        for(int i=0; i<num; i++){
          int ele = random_input(range);
          cout<<"\nInserted : "<<ele;
          tree.insertNode(ele);
        }

        break;

      case 2:

        cout<<"\nEnter key to search : ";
        cin>>key;
        result = tree.find(key);
        cout<<(result != nullptr ? "\nFound" : "\nNot Found")<<"\n";
        break;

      case 3:
        cout<<"\n Enter key to delete : ";
        cin>>key;
        cout<<"\nDeleting Node..";
        result = tree.find(key);
        if(result!=nullptr){
          tree.deleteNode(key);
          cout<<"\nSuccessful";
        }
        else{
          cout<<"\nNot Found";
        }
        break;

      case 4:
        cout<<"\nEuler Tour Traversal : ";
        tree.eulerTourHelp();
        break;

      case 5:
        cout<<"\nPreorder Traversal : ";
        tree.preorder();
        cout<<"\nInorder Traversal : ";
        tree.inorder();
        cout<<"\nPostorder Traversal : ";
        tree.postorder();
        break;

      case 6:
        cout<<"\nEnter key to find Max Value in Subtree : ";
        cin>>key;
        result = tree.find(key);
        if(result!=nullptr){
          cout<<'\n'<<tree.maxValueNode(result)->data;
        }
        else{
          cout<<"\nNot Found";
        }


        break;

      case 7:
        cout<<"\nEnter key to find Min Value in Subtree : ";
        cin>>key;
        result = tree.find(key);
        if(result!=nullptr){
          cout<<'\n'<<tree.minValueNode(result)->data;
        }
        else{
          cout<<"\nNot Found";
        }
        break;

      case 8:
        cout<<"\nEnter key to find Predecessor : ";
        cin>>key;
        result = tree.find(key);
        if(result!=nullptr){
          cout<<'\n'<<tree.getPredecessor(result)->data;
        }
        else{
          cout<<"\nNot Found";
        }
        break;

      case 9:
        cout<<"\nEnter key to find Successor : ";
        cin>>key;
        result = tree.find(key);
        if(result!=nullptr){
          cout<<'\n'<<tree.getSuccessor(result)->data;
        }
        else{
          cout<<"\nNot Found";
        }

        break;

      default:
        cout<<"\nExiting ....";
        return 0;
    }

  }



  return 0;
}


