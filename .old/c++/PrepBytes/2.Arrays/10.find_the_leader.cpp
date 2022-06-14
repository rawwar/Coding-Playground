#include <iostream>

using namespace std;

int main()
{

    int N, size;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> size;
        int arr[size];
        int max;
        for (int j = 0; j < size; j++)
        {
            cin >> arr[j];
        }
        max = arr[size-1];
        cout << max << " ";
        for (int j = size-2; j >= 0; j--)
        {
            int k;
            if(arr[j] >= max ){
                cout << arr[j] << " ";
                max = arr[j];
            }
            
        }
        cout << endl;
    }
}