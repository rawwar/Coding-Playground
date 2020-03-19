#include <iostream>

using namespace std;

int main()
{

    int N, count, last_digit;
    long x;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> x;
        count = 0;
        if (x == 0)
        {
            cout << -1 << endl;
            continue;
        }
        last_digit = x % 10;
        if (last_digit == 5)
        {
            cout << 1;
        }
        else if (last_digit == 0)
        {
            cout << 0;
        }
        else
        {
            cout << -1;
        }
        cout << endl;
    }
}