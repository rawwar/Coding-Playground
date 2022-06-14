#include <iostream>

using namespace std;

int main()
{
    int N, size;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> size;
        int res = 1;
        int temp;
        for (int j = 0; j < size; j++)
        {
            cin >> temp;
            res = res * temp;
        }
        cout << res << endl;
    }
}