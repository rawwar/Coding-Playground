#include <iostream>

using namespace std;

int main()
{
    int n, result, temp;
    cin >> n;
    result = 0;
    while (n > 0)
    {
        temp = n % 10;
        result = result * 10 + temp;
        n = n / 10;
    }
    cout << result;
}