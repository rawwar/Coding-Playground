#include <iostream>

int main(int argc, char const *argv[])
{
    /* code */
    int x, y;
    std::cin >> x >> y;
    if (x < y)
    {
        std::cout << x << " is smaller than " << y;
    }
    else if (x > y)
    {
        std::cout << x << " is greater than " << y;
    }
    else
    {
        std::cout << x << " is equal to " << y;
    }

    return 0;
}
