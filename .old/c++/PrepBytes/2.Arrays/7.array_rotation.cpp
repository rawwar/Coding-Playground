#include <iostream>

using namespace std;

int main()
{
    int T, N, K;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        cin >> N >> K;
        int arr[N];
        for (int j = 0; j < N; j++)
        {
            cin >> arr[(j + K) % N];
        }
        for (int j = 0; j < N; j++)
        {
            cout << arr[j] << " ";
        }

        cout << endl;
    }
}