#include <iostream>

using namespace std;

int main()
{
    int N, X, count, val;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> X;
        count = 0;
        while (X > 10)
        {
            val = X % 10;
            if (val == 5)
            {
                count++;
            }
            X = X / 10;
        }
        if (X == 5)
        {
            count++;
        }
        cout << count << endl;
    }
}