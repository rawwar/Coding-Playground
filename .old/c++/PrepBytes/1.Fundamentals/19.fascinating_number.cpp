#include <iostream>

using namespace std;

int check_repeating(int);

int main()
{
    int N, num;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> num;
        while (1)
        {
            num++;
            if (check_repeating(num) == 0)
            {
                continue;
            }
            else
            {
                cout << num << endl;
                break;
            }
        }
    }
}

int check_repeating(int num)
{
    int ones, tens, hundreds, thousands;
    ones = num % 10;
    num = num / 10;
    tens = num % 10;
    num = num / 10;
    hundreds = num % 10;
    num = num / 10;
    thousands = num % 10;
    // cout << thousands << hundreds << tens << ones << endl;

    if (ones != tens && ones != hundreds && ones != thousands)
    {
        if (tens != hundreds && tens != thousands)
        {
            if (hundreds != thousands)
            {
                return 1;
            }
        }
    }
    return 0;
}
