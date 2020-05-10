#include <iostream>

using namespace std;

int gcd(int, int);

int main()
{

    int N, l, r, res;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> l >> r;
        res=l;
        for (int j = l+1; j <= r; j++)
        {
            res = gcd(j, res);
            if (res == 1)
            {
                break;
            }
        }
        cout << res << endl;
    }
}

int gcd(int a, int b)
{
    if (b == 0)
    {
        return a;
    }
    else
    {
        return gcd(b, a%b);
    }
}
