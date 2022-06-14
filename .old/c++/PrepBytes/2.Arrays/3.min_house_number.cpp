#include <iostream>

using namespace std;

int main()
{
    int N, size;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        int arr[size];
        cin >> size;
        for (size_t i = 0; i < size; i++)
        {
            cin >> arr[i];
        }
        int lowest = 0;
        for (int i = 0; i < size; i++)
        {
            if (arr[i] < arr[lowest])
            {
                lowest = i;
            }
        }
        cout << lowest << endl;
    }
}