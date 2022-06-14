#include <iostream>

using namespace std;

int main()
{
    int N, a, b, c, n, cur, score;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> a >> b >> c >> n;
        cout << a << " " << b << " " << c << " ";
        cur = 4;
        score = 0;
        while (cur <= n)
        {
            score = a + b + c;
            a = b;
            b = c;
            c = score;
            cout << c << " ";
            cur++;
        }
        cout << endl;
    }
}