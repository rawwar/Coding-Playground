#include <iostream>

using namespace std;

int main()
{

    int N;
    cin >> N;
    for (int k = 0; k < N; k++)
    {   
        int size;
        cin >> size;


        int arr[size];
        for (int i = 0; i < size; i++)
        {
            cin >> arr[i];
        }   
        
        int i, j;
        for (i = 0, j = size-1; i < ((size+1)/2) && i!=j; i++, j--)
        {

            cout << arr[j] << " " << arr[i] << " ";
        }
        if(size%2 !=0){
        cout << arr[i] << endl;
        }
    }
}