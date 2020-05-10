#include <iostream>

using namespace std;

void swap_numbers(int &a, int &b);
void display(int *array,int size);
void merge(int *array, int l, int m, int r);
void mergeSort(int *array, int l, int r);

int main(){
    int n;
    cout << "Enter number of elements in the array :";
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << "Array before sorting : ";
    display(arr,n);
    mergeSort(arr, 0, n-1);
    cout << "Array after sorting : ";
    display(arr, n);


    

}

void display(int *array, int size){
    for (int i = 0; i < size; i++)
    {
        cout << array[i] << " ";
    }
    cout << endl;
    
}


void mergeSort(int* arr, int l, int r){
    int m;
    if( l < r){
        int m = l + (r - l)/2;
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);
        merge(arr, l , m , r);

    }
}

void merge(int* arr, int l, int m, int r){
    int i,j,k, nl, nr;
    nl = m - l +1;
    nr = r - m;
    int larr[nl];
    int rarr[nr];

    for ( i = 0; i < nl; i++)
    {
        larr[i] = arr[l+i];
    }
    for ( i = 0; i < nr; i++)
    {
        rarr[i] = arr[m+i+1];
    }

    i=0, j=0, k = l;

    while( i < nl && j < nr){
        if (larr[i] < rarr[j]){
            arr[k] = larr[i];
            i++;

        }else{
            arr[k] = rarr[j];
            j++;
        }
        k++;
    }

    while( i < nl){
        arr[k] = larr[i];
        i++;
        k++;
    }

    while (j < nr){
        arr[k] = rarr[j];
        j++;
        k++;
    }
    
    

}