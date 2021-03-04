/*
4. Write a program to implement the breadth first search(BFS) and depth first search(DFS) in graph.
*/

#include<bits/stdc++.h>

typedef long long int ll;
using namespace std;
class Graph{
    int n;
    unordered_map<int,vector<int>> adjList;
    public:
    Graph(int N){
        n=N;
        unordered_map<int,vector<int>> adjList(n);
    }


    void addEdge(int u, int v){
        adjList[u].push_back(v);
        adjList[v].push_back(u);
    }
    void printGraph(){
        cout<<"---Adjacency List---\n";
        for(int i=1; i<=n; i++){
            cout<<i<<" -> ";
            for(auto j: adjList[i])
                cout<<j<<",";
            cout<<'\n';
        }
    }

    void bfstraversal(int ele){

        queue<int> q;
        int vis[n+1]={0};
        vis[ele]=1;
        q.push(ele);

        while(q.size()>0){
            ele = q.front();
            cout<<ele<<"->";
            q.pop();
            for(auto i: adjList[ele]){
                if(vis[i]==0){
                    vis[i]=1;
                    q.push(i);
                }
            }
        }

    }
    void dfshelper(int ele, int vis[]){

        cout<<ele<<"->";
        vis[ele] = 1;

        for(int i=0; i<adjList[ele].size(); i++){
            int curr=adjList[ele][i];
            if(vis[curr]==0)
                dfshelper(curr,vis);
        }
    }
    void dfstraversal(int ele){
        int vis[n+1]={0};
        dfshelper(ele,vis);
    }
};


int main()
{

    /*
        MY GRAPH
        1-----2
        |\    | \
        | \   |  \
        |  \  |   3
        |   \ |  /
        |    \| /
        5-----4

    */

    Graph obj(5);
    obj.addEdge(1,2);
    obj.addEdge(2,3);
    obj.addEdge(3,4);
    obj.addEdge(2,4);
    obj.addEdge(1,4);
    obj.addEdge(1,5);
    obj.addEdge(5,4);

    obj.printGraph();
    cout<<"--BFSTRAVERSAL--\n";
    obj.bfstraversal(1);

    cout<<"\n--DFSTRAVERSAL--\n";
    obj.dfstraversal(1);



    return 0;

}
