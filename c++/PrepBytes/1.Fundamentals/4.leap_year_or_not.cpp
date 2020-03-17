#include <iostream>

bool check_leap_year(int);

int main(int argc, char const *argv[])
{
    int N, year;
    std::cin >> N;
    for (int i = 0; i < N; i++)
    {
        std::cin >> year;
        bool check = check_leap_year(year);
        if (check)
        {
            std::cout << "Yes" << std::endl;
        }
        else
        {
            std::cout << "No" << std::endl;
        }
    }
    return 0;
}

bool check_leap_year(int year)
{
    if (year % 4 == 0)
    {
        if (!(year % 100 == 0))
        {
            return true;
        }
        else
        {
            if (!(year % 400 == 0))
            {
                return false;
            }
        }
    }
    else
    {
        return false;
    }
    return true;
}