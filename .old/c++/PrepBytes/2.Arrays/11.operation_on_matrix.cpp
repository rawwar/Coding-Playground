#include <iostream>

using namespace std;

int main(){
    int N,M ;
    cin >> M >> N;

    int arr1[M][N];
    int arr2[M][N];

    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> arr1[i][j];
        }
        
    }
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> arr2[i][j];
        }
        
    }

    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cout << arr1[i][j] + arr2[i][j] << " ";
        }
        cout << endl;
        
    }
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            int sum = 0;
            for (int k = 0; k < N; k++)
            {
                sum += arr1[i][k] * arr2[k][j];
            }
            cout << sum << " ";
            
        }
        cout << endl;
        
    }
    
}