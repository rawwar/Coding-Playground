#include <iostream>

using namespace std;

int main()
{

    int N;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        int size;
        cin >> size;
        int arr[size];

        for (int j = 0; j < size; j++)
        {
            cin >> arr[j];
        }
        int result;
        int flag = 0;
        cin >> result;
        for (int j = 0, k = size - 1; j < size && k >= 0 && j < k;)
        {
            if (arr[j] + arr[k] > result)
            {
                k--;
            }
            else if (arr[j] + arr[k] < result)
            {
                j++;
            }
            else
            {
                cout << j << " " << k << endl;
                flag = 1;
                break;
            }
        }
        if (flag == 0)
        {
            cout << "no answer" << endl;
        }
    }
}