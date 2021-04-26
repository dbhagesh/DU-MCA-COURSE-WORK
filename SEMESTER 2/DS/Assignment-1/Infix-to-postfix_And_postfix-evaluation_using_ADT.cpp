#include<bits/stdc++.h>
#include "STACK.h"
using namespace std;

//Function to check operand
bool isOperand(char ch){
	return ((ch>='a' && ch<='z') || (ch>='A' && ch<='Z') || (ch>='1' && ch<='9'));
}
//Function to check operator
bool isOperator(char ch){
	return (ch == '+' || ch == '-' || ch == '/' || ch == '*' || ch == '^');
}

//Function to return precedence of operator
int opPrecedence(char op){
	switch (op) {
	    case '+':
	    case '-':
	      return 1;

	    case '*':
	    case '/':
	      return 2;

	    case '^':
	      return 3;

	    case '(':
	    case ')':
	      return 0;

	    default:
	      return -1;
  }
}

//Function to convert infix to postfix
string infixToPostfix(string infix){
	string postfix;

	//Using ADT defined in STACK.h header file
	mystack<char> op_stack;

	//Scanning the expression
	for(int i=0; i<infix.length(); i++){

		//If operand push to postfix string
		if(isOperand(infix[i]))
			postfix.push_back(infix[i]);

		//If ( push to the stack
		else if(infix[i]=='(')
			op_stack.push(infix[i]);
		
		//if ) pop all the stack and push to the postfix expression
		else if(infix[i]==')'){
			while(!op_stack.isEmpty() and op_stack.top()!='('){
				postfix.push_back(op_stack.pop());
			}

			if(op_stack.isEmpty()){
				throw "Enter a valid expression.";
			}
			else op_stack.pop();
		}
		else if(isOperator(infix[i])){
			//If stack is empty
			if(op_stack.isEmpty()) op_stack.push(infix[i]);
			//If precedence of current operator > the precendance of operator on top of stack
			else if(opPrecedence(infix[i])>opPrecedence(op_stack.top())) op_stack.push(infix[i]);
			//If precedence of current <= top of stack, pop out and append until 
			//precedence of current > top of stack
			else{
				do{
					postfix.push_back(op_stack.pop());
				}while(!op_stack.isEmpty() && opPrecedence(infix[i])<=opPrecedence(op_stack.top()));
				op_stack.push(infix[i]);
			}
		}
	}
	//If stack is not empty pop and append to postfix
	while(!op_stack.isEmpty()){
		postfix.push_back(op_stack.pop());
	}

	return postfix;
}

//Function to evaluate postfix expression
int evaluatePostfix(string postfix){

	//Using the ADT defined in STACK.h header file
	mystack<int> stack; 
	//Scaning expression
	for(int i=0; i<postfix.length(); i++){

		//If operand push to stack
		if(isOperand(postfix[i])) stack.push(postfix[i]-'0');
		else{
			//Pop two values
			int val1 = stack.pop();
			int val2 = stack.pop();

			//Perform operation on two values and push the result
			switch(postfix[i]){
				case '+': stack.push(val1+val2); break;
				case '-': stack.push(abs(val1-val2)); break;
				case '*': stack.push(val1*val2); break;
				case '/': stack.push(val2/val1); break;

			}
		}
	}
	//Pop the final result
	return stack.pop();
}
int main()
{
	
	string infix;
	cout<<"Use expression with integers or floats as operands.\n";
	cout<<"Using operands as chars wont result in 'evaluation of postfix expression'.\n";

	cout<<"---Program to convert Infix to Postfix expression and evalauting it---\n\n";
	cout<<"Enter Infix expression: ";
	cin>>infix;

	try{
		string postfix = infixToPostfix(infix);
		cout<<"\nPostfix Expression : "<<postfix<<'\n';

		cout<<"\nEvaluated Postfix Expression : ";
		cout<<evaluatePostfix(postfix);
		
	}catch(const char* err){
		cerr<<"\nError: "<<err;
	}catch(...){
		cout<<"\nError";
	}
	
	return 0;

}
