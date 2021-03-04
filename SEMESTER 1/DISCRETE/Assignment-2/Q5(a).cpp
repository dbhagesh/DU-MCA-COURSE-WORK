/*
5. Write a program to identify the Eulerian and Hamiltonian circuits in a given graph.
This program contains the eulerian part only.

Checks if the graph is connected and if the graph contains no oddDegree vertexes then it is euler circuit.
*/


#include<bits/stdc++.h>
using namespace std;
int n;
int vertex=0;
unordered_map<int,vector<int>> adjList(n);
void addEdge(int u, int v){
    vertex++;
    adjList[u].push_back(v);
    adjList[v].push_back(u);
}
void dfshelper(int ele,int vis[]){

    vis[ele] = 1;

    for(int i=0; i<adjList[ele].size(); i++){
        int curr=adjList[ele][i];
        if(vis[curr]==0)
            dfshelper(curr,vis);
    }
}

bool isConnected(){
    int vis[n+1]={0};
    dfshelper(1,vis);
    for(int i=1; i<=n; i++) if(vis[i]==0)
        return false;

    return true;
}

void isEulerian(){

    if(!isConnected()){
        cout<<"Graph is not connected. Therefore it isn't a Eulerian Path/Circuit.";
        return;
    }

    int degree[n+1]={0};

    for(int i=1; i<=n; i++){
        for(auto j: adjList[i])
            degree[i]++;
    }

    int oddDegree=0;
    for(auto i: degree) if(i&1==1) oddDegree++;


    if(oddDegree==2) cout<<"Eulerian path";
    else if(oddDegree==0) cout<<"Eulerian circuit as well as Euler path";
    else cout<<"Not Eulerian path/Circuit";

}

int main()
{
    cout<<"Enter number of vertex: ";
    cin>>n;


    addEdge(1,2);
    addEdge(2,3);
    addEdge(3,4);
    addEdge(2,4);
    addEdge(1,4);
    addEdge(1,5);
    addEdge(5,4);
    //addEdge(6,7);

    isEulerian();


}
