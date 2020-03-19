#include <iostream>

using namespace std;

int main()
{
    int x, y, z;
    cin >> x >> y >> z;
    if (x <= y && x <= z)
    {
        if (y < z)
        {
            cout << y;
        }
        else
        {
            cout << z;
        }
    }
    else if (y <= x && y <= z)
    {
        if (x < z)
        {
            cout << x;
        }
        else
        {
            cout << z;
        }
    }
    else
    {
        if (y < x)
        {
            cout << y;
        }
        else
        {
            cout << x;
        }
    }
}