/*
2. Write a program to find a Preorder, Inorder and Postorder traversal of 3-ary Tree.
*/

#include<bits/stdc++.h>
using namespace std;

struct Node{
    int data;
    Node *left,*right,*mid;
    Node(int data){
        this->data = data;
        this->left = NULL;
        this->mid = NULL;
        this->right = NULL;
    }
};
void printPreorder(Node * node){
    if(node == NULL) return;

    cout<<node->data<<" ";

    printPreorder(node->left);
    printPreorder(node->mid);
    printPreorder(node->right);
}
void printInorder(Node * node){

    if(node == NULL) return;

    printInorder(node->left);
    printInorder(node->mid);

    cout<<node->data<<" ";

    printInorder(node->right);
}
void printPostorder(Node * node){

    if(node == NULL) return;

    printPostorder(node->left);
    printPostorder(node->mid);
    printPostorder(node->right);

    cout<<node->data<<" ";
}

int main()
{
    /*
       My 3-ary tree(REMAINING LEAFS ARE NULL )
            1
          / | \
         2  3  4
        /|\     \
       5 6 7     8

    */

    Node *root = new Node(1);
    root->left = new Node(2);
    root->left->left = new Node(5);
    root->left->mid = new Node(6);
    root->left->right = new Node(7);
    root->mid = new Node(3);
    root->right = new Node(4);
    root->right->right = new Node(8);


    int ch;
    while(true){
        cout<<"\nEnter\n1.PREORDER\n2.INORDER\n3.POSTORDER\n";
        cin>>ch;
        if(ch==1) cout<<"PREORDER->",printPreorder(root);
        else if(ch==2) cout<<"INORDER->",printInorder(root);
        else if(ch==3) cout<<"POSTORDER->",printPostorder(root);
        else break;
    }


    return 0;

}
