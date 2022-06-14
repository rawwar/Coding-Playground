#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int N, x, total, temp;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        total = 1;
        cin >> x;
        for (int j = 2; j <= sqrt(x); j++)
        {
            if (x % j == 0)
            {
                if (x / j == j)
                {
                    temp = j;
                }
                else
                {
                    temp = j + x / j;
                }

                total = total + temp;
            }
        }

        if (total == x and x != 1)
        {
            cout << "true";
        }
        else
        {
            cout << "false";
        }
        cout << endl;
    }
}