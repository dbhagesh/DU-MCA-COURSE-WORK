/*

Hamiltonian circuits in a given graph.
This program contains the Hamiltonian circuit only.

Uses backtracking approach to traverse the graph to print all possible hamiltonian circuits
*/
#include<bits/stdc++.h>
using namespace std;

#define V 5
void printPath(int path[]){
    cout<<"Path: ";
    for(int i=0; i<V; i++) cout<<path[i]<<" ";

    cout<<endl;
}

bool isSafe(int v, bool graph[V][V],int path[],int pos){

    if(graph[path[pos-1]][v]==0) return false;

    for(int i=0; i<pos; i++) if(path[i]==v) return false;

    return true;
}
void hamHelper(bool graph[V][V],int path[],int pos){
    if(pos == V ){
        if(graph[path[pos-1]][path[0]]) printPath(path);


    }

    for(int v=1; v<V; v++){
        if(isSafe(v,graph,path,pos)){
            path[pos]=v;

            hamHelper(graph,path,pos+1);

            path[pos]=-1;
        }
    }




}
void hamiltonian(bool graph[V][V]){
    int path[V];
    memset(path,-1,sizeof(path));

    path[0]=0;

    hamHelper(graph,path,1);



}
int main()
{

    /*

    My graph 
    0----1------2
    |   /|      /
    |  / |    /
    | /  |  /
    |/   |/
    3--- 4
    */
    bool graph[V][V] = {{0, 1, 0, 1, 0},
                        {1, 0, 1, 1, 1},
                        {0, 1, 0, 0, 1},
                        {1, 1, 0, 0, 1},
                        {0, 1, 1, 1, 0}};

    hamiltonian(graph);
    return 0;

}
