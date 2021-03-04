#include<bits/stdc++.h>
using namespace std;

void merge(int arr[], int l, int m, int r){
    int s1 = m-l+1; int s2 = r-m;
    int a[s1],b[s2];

    for(int i=0; i<s1; i++) a[i] = arr[l+i];
    for(int i=0; i<s2; i++) b[i] = arr[m+i+1];
    int i=0,j=0,k=l;
    while(i<s1 && j<s2){
        if(a[i]<=b[j]) arr[k++]=a[i++];
        else arr[k++] = b[j++];
    }

    while(i<s1) arr[k++]=a[i++];
    while(j<s2) arr[k++]=b[j++];

}

void mergesort(int arr[], int l, int r){

    if(l<r){
        int m = (l+r)/2;
        mergesort(arr,0,m);
        mergesort(arr,m+1,r);

        merge(arr,l,m,r);

    }
}
int main()
{
    int n;
    cout<<"Enter the size of the array: ";
    cin>>n;

    int arr[n];
    for(auto &i: arr) cin>>i;

    mergesort(arr,0,n-1);
    cout<<"Sorted Array: ";
    for(auto &i: arr) cout<<i<<" ";

    return 0;

}
