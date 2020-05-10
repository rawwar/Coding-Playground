#include <iostream>

using namespace std;

int main()
{
    int N;
    cin >> N;
    int even[N];
    int odd[N];
    int temp, even_counter = 0, odd_counter = 0;
    for (int i = 0; i < N; i++)
    {
        cin >> temp;
        if (temp % 2 == 0)
        {
            even[even_counter] = temp;
            even_counter++;
        }
        else
        {
            odd[odd_counter] = temp;
            odd_counter++;
        }
    }
    for (int i = 0; i < even_counter; i++)
    {
        cout << even[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < odd_counter; i++)
    {
        cout << odd[i] << " ";
    }
}