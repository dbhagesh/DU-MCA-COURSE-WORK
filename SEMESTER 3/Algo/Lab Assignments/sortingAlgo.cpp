#include<bits/stdc++.h>
#include <chrono>
#include <unistd.h>
#define int long long
using namespace std::chrono;
using namespace std;

// Iterative Insertion Sort
void insertion_iterative(vector<int> arr, int n) {

	int key, j, comp = 0;
	auto start = chrono::high_resolution_clock::now();


	for(int i = 1; i < n; i++) {

		key = arr[i];
		j = i - 1;

		while(j>=0 and ++comp and arr[j] > key) {
			arr[j+1] = arr[j];
			j--;
		}

		arr[j+1] = key;
	}

	auto stop = chrono::high_resolution_clock::now();
	auto duration = chrono::duration_cast<nanoseconds>(stop - start);

	cout<<"Number of comparisons : "<<comp<<'\n';
	cout<<"Executed In: "<<duration.count()<<" ms\n\n";

}

// Recursive Insertion Sort
void insertion_recursive(vector<int> arr, int n, int &comp) {
	int key, j;

    if(n <=1 ) {
        cout<<"Number of comparisons : "<<comp<<'\n';
        comp = 0;
        return;
    }

	insertion_recursive(arr, n-1, comp);

    key = arr[n-1];
    j = n - 2;

    while(j>=0 and ++comp and arr[j] > key) {
        arr[j+1] = arr[j];
        j--;
    }

    arr[j+1] = key;


}
// Merge Sort

int32_t main()
{

	//Number of elements
	int n; cin>>n;

	//Inputting Dataset
	vector<int> a1(n)
	,a2(n)
	,a3(n);

	int t = 3;

	while(t--) {

		if(t == 2) {
			for(int i = 0; i < n; i++ ){
                a1[i] = i + 1;
			}
		}
		else if(t == 1) {
			for(int i = 0; i < n; i++){
                a2[i] = 100-i;
			}
		}
		if(t == 0) {
			for(int i = 0; i < n; i++ ){
                a3[i] = i + 1;
			}
			random_shuffle(a3.begin(), a3.end());
			for(auto i : a3) cout<<i<<endl;
		}

	}



	while(true) {

		cout<<"\n\n --Menu-- \n\n";
		cout<<"1 : Insertion Iterative\n";
		cout<<"2 : Insertion Recursive\n";
		cout<<"3 : Merge Sort\n";
		cout<<"4 : Quick Sort\n";
		cout<<"Enter Input : ";
		int input, comp = 0;	cin>>input;
		cout<<endl;
		switch(input) {

			case 1 :

				cout<<" -| Iterative Insertion Sort |- \n\n";

				cout<<" - Ascending Sorted Data\n";
				insertion_iterative(a1, n);

				cout<<" - Descending Sorted Data\n";
				insertion_iterative(a2, n);

				cout<<" - Mixed Data\n";
				insertion_iterative(a3, n);

                break;


			case 2 :

				cout<<" -| Recursive Insertion Sort |- \n\n";

				cout<<" - Ascending Sorted Data\n";
				insertion_recursive(a1, n, comp);

                cout<<" - Descending Sorted Data\n";
				insertion_recursive(a2, n, comp);

				cout<<" - Mixed Data\n";
                insertion_recursive(a3, n, comp);

                break;

			case 3 :
				cout<<"Merge";

                break;

			case 4 :
				cout<<"Quick";
                break;

			default :
                exit(0);



		}
	}


	return 0;

}
