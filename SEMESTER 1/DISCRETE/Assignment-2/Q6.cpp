/*
6. Write a program to identify that the given graph is planar or not.
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

    if(isConnected() && n<=(3*vertex-6)) cout<<"Yes, it is a planar graph.";
    else cout<<"No, it is not planar graph.";


}
