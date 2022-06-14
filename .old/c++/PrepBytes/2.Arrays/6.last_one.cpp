#include <iostream>

using namespace std;

int main()
{
    int N, size;
    int index;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        index = -1;
        cin >> size;
        int arr[size];
        for (int j = 0; j < size; j++)
        {
            cin >> arr[j];
            if (arr[j] == 1)
            {
                index = j;
            }
        }
        cout << index << endl;
    }
}